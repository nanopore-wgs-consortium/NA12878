import pandas as pd
import h5py
from collections import defaultdict
from tqdm import tqdm
import sys
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')


def die(message, status=1):
    """Print an error message and call sys.exit with the given status, terminating the process"""
    print(message, file=sys.stderr)
    sys.exit(status)


def get_dtypes(hdf5_path, enum_field):
    if h5py.check_dtype(enum=hdf5_path.dtype[enum_field]):
        # data_dtype may lose some dataset dtypes if there are duplicates of 'v'
        return {v: k for k, v in h5py.check_dtype(enum=hdf5_path.dtype[enum_field]).items()}


def get_data(bulkfile_path, seq_sum_path, read_list=None, time=2, name=None, read_pos='end_time'):
    """
    Get classification data from start or end of reads in a bulkfile
    Parameters
    ----------
    bulkfile_path : str
        Path to bulk FAST5 file
    ss : pd.DataFrame
        Sequencing_summary file as pandas DataFrame
    read_list : list
        List of reads to get classifications for
    time : numeric (int or float)
        Time surrounding the end of a read to get classifications
    name : str
        (Optional) label to add onto returned data, useful for grouping
    read_pos : str
        Either 'start_time' or 'end_time' for classifications at start or end of reads

    Returns
    -------
    list
        list of lists; with columns ['read_id', 'time', 'label', 'name']
    """
    ss = pd.read_csv(seq_sum_path, sep='\t', usecols=['run_id', 'read_id', 'channel', 'start_time', 'duration'])
    bf = h5py.File(bulkfile_path, 'r')
    sf = int(bf["UniqueGlobalKey"]["context_tags"].attrs["sample_frequency"].decode('utf8'))
    run_id = bf["UniqueGlobalKey"]["tracking_id"].attrs["run_id"].decode('utf8')
    ss = ss[ss['run_id'] == run_id]
    ss['end_time'] = ss['start_time'] + ss['duration']
    # ss['end_time'] = ss['end_time']
    conv = {'acquisition_raw_index': 'read_start',
            'summary_state': 'modal_classification'}
    if read_list is not None:
        ss = ss[ss['read_id'].isin(read_list)]
    channels = ss['channel'].unique()
    # get label dtypes
    labels_dt = get_dtypes(
        bf['IntermediateData']['Channel_' + str(channels[0])]['Reads'], 'modal_classification'
    )
    labels_dt.update(
        get_dtypes(bf['StateData']['Channel_' + str(channels[0])]['States'], 'summary_state')
    )
    int_data = defaultdict()
    state_data = defaultdict()
    b = []
    for ch in tqdm(channels):
        path = bf['IntermediateData']['Channel_' + str(ch)]['Reads']
        for f in ['read_id', 'modal_classification', 'read_start']:
            int_data[f] = path[f]
        path = bf['StateData']['Channel_' + str(ch)]['States']
        for f in ['acquisition_raw_index', 'summary_state']:
            state_data[conv[f]] = path[f]
        df = pd.concat([pd.DataFrame(int_data), pd.DataFrame(state_data)], axis=0)
        df['read_id'] = df['read_id'].str.decode('utf8')
        df.sort_values(by='read_start', ascending=True, inplace=True)
        df['read_id'] = df['read_id'].fillna(method='ffill')
        df['modal_classification'] = df['modal_classification'].map(labels_dt)
        df['read_start'] = df['read_start'] / sf
        temp_ss = ss[ss['channel'] == ch]
        for idx, row in temp_ss.iterrows():
            before = df[df['read_start'].between(row[read_pos] - time, row[read_pos], inclusive=False)]
            after = df[df['read_start'].between(row[read_pos], row[read_pos] + time, inclusive=True)]
            for i, r in before.iterrows():
                b.append([row['read_id'],
                          r['read_start'] - row[read_pos],
                          r['modal_classification'],
                          name
                         ])
            for i, r in after.iterrows():
                b.append([row['read_id'],
                          r['read_start'] - row[read_pos],
                          r['modal_classification'],
                          name
                         ])
    bf.close()
    return b


def main():
    if len(sys.argv) < 3:
        die('Usage: python {s} sequencing_summary.txt <path/to/bulkfile/directory>'.format(s=sys.argv[0]))
    files = [[p] for p in Path(sys.argv[2]).iterdir() if p.suffix == '.fast5']
    if not files:
        die('No bulk FAST5 files found in {}'.format(sys.argv[2]))
    for t in files:
        f = h5py.File(t[0], 'r')
        t.append(f["UniqueGlobalKey"]["tracking_id"].attrs["run_id"].decode('utf8'))
        f.close()

    for file_name, run_id in files:
        print('{},\t{}'.format(file_name, run_id))

    print('Collecting ends:')
    filename = 'end_events.csv'
    paginate = False
    for t in files:
        end_data = get_data(t[0], sys.argv[1], time=2, name=t[1], read_pos='end_time')
        df = pd.DataFrame(end_data, columns=['read_id', 'time', 'label', 'comment'])
        if not df.empty and not paginate:
            df.to_csv(filename, sep=',', header=True, index=False)
            paginate = True
        elif not df.empty and paginate:
            with open(filename, 'a') as file:
                df.to_csv(file, sep=',', header=False, index=False)
        else:
            print('df is empty')

    print('Collecting starts:')
    filename = 'start_events.csv'
    paginate = True
    for t in files:
        end_data = get_data(t[0], sys.argv[1], time=2, name=t[1], read_pos='start_time')
        df = pd.DataFrame(end_data, columns=['read_id', 'time', 'label', 'comment'])
        if not df.empty and not paginate:
            df.to_csv(filename, sep=',', header=True, index=False)
            paginate = True
        elif not df.empty and paginate:
            with open(filename, 'a') as file:
                df.to_csv(file, sep=',', header=False, index=False)
        else:
            print('df is empty')


if __name__ == '__main__':
    main()
