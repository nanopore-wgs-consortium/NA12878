import signal
import sys
from collections import OrderedDict
from pathlib import Path

from ont_fast5_api import fast5_file
import pandas as pd
import numpy as np
from bokeh.layouts import row, widgetbox
from bokeh.models import Select, RadioButtonGroup, TextInput
from bokeh.plotting import curdoc, figure


def init_wdg_dict(read_list):
    """Generate the widget dictionary"""
    widget_dict = OrderedDict()
    widget_dict['read_list'] = Select(title="Select read to visualise:", options=read_list)
    widget_dict['signal_position'] = RadioButtonGroup(labels=['START', 'END'], active=1)
    widget_dict['scaled_signal'] = RadioButtonGroup(labels=['SCALED (pA)', 'UNSCALED (raw)'], active=0)
    widget_dict['plot_width'] = TextInput(title='Plot Width (px)', value=str(data['PLOT_WIDTH']))
    widget_dict['plot_height'] = TextInput(title='Plot Height (px)', value=str(data['PLOT_HEIGHT']))

    widget_dict['read_list'].on_change('value', update_file)
    widget_dict['signal_position'].on_change('active', update_toggle)
    widget_dict['scaled_signal'].on_change('active', update_scale)
    widget_dict['plot_width'].on_change('value', update_size_w)
    widget_dict['plot_height'].on_change('value', update_size_h)
    return widget_dict


def update_file(attr, old, new):
    """Update files and re-plot lines"""
    data['ORIGINAL_FN'], data['INTERVAL_FN'] = df[df['read_id'].eq(new)][['filename', 'bv_filename']].values.tolist()[0]
    update()


def update():
    layout.children[1] = create_figure(signal_from_read(data['ORIGINAL_FN'], scale=data['SCALE_SIGNAL']),
                                       signal_from_read(data['INTERVAL_FN'], scale=data['SCALE_SIGNAL']),
                                       position=data['SIGNAL_POSITION'])


def update_size_w(attr, old, new):
    data['PLOT_WIDTH'] = int(new)
    update()


def update_size_h(attr, old, new):
    data['PLOT_HEIGHT'] = int(new)
    update()


def update_toggle(attr, old, new):
    if new == 0:    # START
        data['SIGNAL_POSITION'] = 'start'
    elif new == 1:  # END
        data['SIGNAL_POSITION'] = 'end'
    update()


def update_scale(attr, old, new):
    if new == 0:    # SCALED
        data['SCALE_SIGNAL'] = True
    elif new == 1:  # UNSCALED
        data['SCALE_SIGNAL'] = False
    update()


def create_figure(signal_tuple_1, signal_tuple_2, position='end'):
    if position == 'start':
        signal_tuple_1[0] = signal_tuple_2[0]
        signal_tuple_1[1] = np.append(signal_tuple_1[1][::-1],
                                      np.repeat(np.nan, len(signal_tuple_2[1]) - len(signal_tuple_1[1])))[::-1]

    f = figure(tools=['box_zoom', 'pan', 'reset', 'save'], active_drag="box_zoom",
               plot_width=data['PLOT_WIDTH'], plot_height=data['PLOT_HEIGHT'])
    f.yaxis.axis_label = "Signal (pA)" if data['SCALE_SIGNAL'] else "Raw signal"
    f.yaxis.major_label_orientation = "horizontal"
    f.xaxis.axis_label = "Samples"
    f.xaxis.major_label_orientation = np.deg2rad(45)
    f.x_range.range_padding = 0.01
    f.line(x=signal_tuple_1[0], y=signal_tuple_1[1], name='signal_1', line_width=1.5, color='blue', alpha=0.8)
    f.line(x=signal_tuple_2[0], y=signal_tuple_2[1], name='signal_2', line_width=0.5, color='red', alpha=0.5)
    f.outline_line_color = None
    f.toolbar.logo = None
    return f


def signal_from_read(path, scale=False):
    file = fast5_file.Fast5File(Path(Path.cwd() / path), 'r')
    y_data = file.get_raw_data(scale=scale)
    file.close()
    return [list(range(0, len(y_data))), y_data]


def signal_handler(sig, frame):
    """"""
    print('\nCtrl+C caught')
    sys.exit(0)


data = {
    'SIGNAL_POSITION': 'end',
    'PLOT_HEIGHT': 980,
    'PLOT_WIDTH': 980,
    'ORIGINAL_FN': '',
    'INTERVAL_FN': '',
    'SCALE_SIGNAL': True
}

signal.signal(signal.SIGINT, signal_handler)

read_info_txt = sys.argv[1]
# seq_sum_original = sys.argv[2]
# seq_sum_interval = sys.argv[3]
original_path = sys.argv[2]
interval_path = sys.argv[3]
# PLOT_WIDTH = int(sys.argv[6])
# PLOT_HEIGHT = int(sys.argv[7])

if original_path[-1] != '/':
    original_path = original_path + '/'
if interval_path[-1] != '/':
    interval_path = interval_path + '/'

df = pd.read_csv(read_info_txt, sep='\t', usecols=['read_id', 'bv_read_id', 'filename', 'bv_filename'])
# df = df.merge(pd.read_csv(seq_sum_original, sep='\t', usecols=['read_id', 'filename']), on='read_id')
# df = df.merge(pd.read_csv(seq_sum_interval, sep='\t', usecols=['read_id', 'filename']),
#               left_on='bv_read_id', right_on='read_id')
# df = df.drop(columns=['bv_read_id'])
df['filename'] = original_path + df['filename']
df['bv_filename'] = interval_path + df['bv_filename']

controls = widgetbox(list(init_wdg_dict(sorted(df['read_id'].unique().tolist())).values()))
plot = create_figure(([0], [0]), ([0], [0]))
layout = row(controls, plot)

curdoc().add_root(layout)
curdoc().title = "signal_server"
