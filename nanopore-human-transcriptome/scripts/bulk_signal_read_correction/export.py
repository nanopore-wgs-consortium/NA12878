import h5py
import pandas as pd
import numpy as np


def smooth_pore(arr, cutoff=1500):
    m = int(np.mean(arr))
    arr[arr > cutoff] = m
    return arr


def export_read_file(channel, start_index, end_index, bulkfile, output_dir, remove_pore=False):
    """Generate a read FAST5 file from channel and coordinates in a bulk FAST5 file

    Parameters
    ----------
    channel : int
        channel number from bulk FAST5 file
    start_index : int
        start index for read (time in seconds * sample_frequency)
    end_index : int
        end index for read (time in seconds * sample_frequency)
    bulkfile : h5py.File
        bulk FAST5 file opened as an h5py object
    output_dir : str
        output directory, must include trailing slash
    remove_pore : bool
        remove pore-like signal (>1500) from pore trace

    Returns
    -------
    str
        filename of the exported read
    """
    out_filename = bulkfile["UniqueGlobalKey"]["context_tags"].attrs["filename"].decode('utf8')
    out_filename = '{fn}_bulkvis-read_{start}-{end}_ch_{ch}.fast5'.format(
        fn=out_filename,
        start=start_index,
        end=end_index,
        ch=channel
    )
    output_arg = "{dir}{fn}".format(
        dir=output_dir,
        fn=out_filename
    )

    readfile = h5py.File(output_arg, "w")
    read_id_str = "{ch}-{start}-{end}".format(
        ch=channel,
        start=start_index,
        end=end_index
    )
    version_num = 0.6

    ch_num = channel
    ch_str = "Channel_{ch}".format(ch=ch_num)

    ugk = readfile.create_group("UniqueGlobalKey")

    bulkfile.copy('UniqueGlobalKey/context_tags', ugk)
    bulkfile.copy('UniqueGlobalKey/tracking_id', ugk)
    bulkfile.copy("IntermediateData/{ch}/Meta".format(ch=ch_str), ugk)

    readfile["UniqueGlobalKey"]["channel_id"] = readfile["UniqueGlobalKey"]["Meta"]
    readfile["UniqueGlobalKey"]["channel_id"].attrs.create(
        'sampling_rate',
        readfile["UniqueGlobalKey"]["Meta"].attrs["sample_rate"],
        None,
        dtype='Float64'
    )
    del readfile["UniqueGlobalKey"]["Meta"]

    readfile["UniqueGlobalKey"]["channel_id"].attrs.create('channel_number', ch_num, None, dtype='<S4')
    remove_attrs = ["description", "elimit", "scaling_used", "smallest_event", "threshold", "window", "sample_rate"]
    for attr in remove_attrs:
        del readfile["UniqueGlobalKey"]["channel_id"].attrs[attr]

    int_data_path = bulkfile["IntermediateData"][ch_str]["Reads"]
    int_dict = {
        'read_start': int_data_path["read_start"],
        'median_before': int_data_path["median_before"],
        'current_well_id': int_data_path["current_well_id"]
    }
    df = pd.DataFrame(data=int_dict)
    df = df.where(df.read_start > start_index).dropna()
    read_number = 0
    attrs = {
        'duration': {'val': end_index - start_index, 'd': 'uint32'},
        'median_before': {'val': df.iloc[0].median_before, 'd': 'Float64'},
        'read_id': {'val': read_id_str, 'd': '<S38'},
        'read_number': {'val': read_number, 'd': 'uint16'},
        'start_mux': {'val': int(df.iloc[0].current_well_id), 'd': 'uint8'},
        'start_time': {'val': start_index, 'd': 'uint64'}
    }

    dataset = bulkfile["Raw"][ch_str]["Signal"][()]
    if remove_pore:
        dataset = smooth_pore(dataset[start_index:end_index])
    else:
        dataset = dataset[start_index:end_index]

    readfile.create_group('Raw/Reads/Read_{n}'.format(n=read_number))
    readfile.attrs.create('file_version', version_num, None, dtype='Float64')
    # add read_### attrs
    for k, v in attrs.items():
        readfile["Raw"]["Reads"]["Read_{n}".format(n=read_number)].attrs.create(k, v['val'], None, dtype=v['d'])

    ms = [18446744073709551615]
    readfile.create_dataset(
        'Raw/Reads/Read_{n}/Signal'.format(n=read_number),
        data=(dataset),
        maxshape=(ms),
        chunks=True,
        dtype='int16',
        compression="gzip",
        compression_opts=1
    )

    readfile.close()
    return out_filename
