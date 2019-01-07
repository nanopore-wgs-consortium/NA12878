bulk_signal_read_correction
===========================

Table of Contents
=================
 - [Setup environment](#setup-environment)
 - [bulk_signal_read_correction](#bulk_signal_read_correction)
 - [Table of Contents](#table-of-contents)
 - [signal_server](#signal_server)
 - [event_finder.py](#event_finderpy)
 - [export.py](#exportpy)
 - [make_reads.py](#make_readspy)


Setup environment
=================
To set up a compatible environment, create a python3 virtual environment:

```bash
$ python3 -m venv path/to/env
```

Activate the environment:

```bash
$ . path/to/env/bin/activate
```

Install required packages:

```bash
$ pip install -r requiremnts.txt
```

signal_server
=============
The signal server is a small [bokeh]() server that will display original signal traces, overlaid with 
extended signal traces. This is primarily for checking that the newly generated files are extensions of 
the original reads.
```bash
$ bokeh serve signal_server --show --args <folder>/ends_read_info.txt <folder>/ends/original/fast5/ <folder>/ends/fast5/
```
OR
```bash
$ bokeh serve signal_server --show --args <folder>/starts_read_info.txt <folder>/starts/original/fast5/ <folder>/starts/fast5/
```

event_finder.py
===============
`event_finder.py` is the python script that extracts MinKNOW event information from 
bulk FAST5 files in the surrounding two seconds at either the starts or ends of reads (as 
determined by the sequencing_summary.txt). The first parameter is the sequencing_summary.txt file
and the second parameter is the path to the bulk FAST5 files.
### Usage:
```bash
$ python3 event_finder.py sequencing_summary.txt <path/to/bulkfile/directory>
``` 

### Output
Writes two files, `end_events.csv` and `start_events.csv` containing the events seen surrounding the ends
and starts of reads respectively.

export.py
=========
`export.py` is a module that can export arbitrary regions of a bulk FAST5 file as call-able read FAST5
files. It is used here to generate 'corrected' read files that extend past the end point decided by 
MinKNOW.

make_reads.py
=============
`make_reads.py` is the python script that will identify abnormally starting or ending reads, through the 
absence of `['pore', 'inrange', 'good_single', 'unblocking']` classifications in the preceding or following 
two seconds of target reads respectively.  
To recover signal their must be a bulk FAST5 file available for the target reads.

```bash
$ python make_reads.py -s <sequencing_summary_files> --start-events start_events.csv --end-events end_events.csv --targets <targets.txt> --bulk-files <path/to/*.fast5> -o <output_name>
```

### Output
Writes a folder structure as so:
```bash
<output_name>/
  ends_filenames.txt
  ends_read_info.txt
  starts_filenames.txt
  starts_read_info.txt
  ends/
   | fast5/
  starts/
   | fast5/
```

### Collecting original reads
The original read files created by MinKNOW can be downloaded using the `curl_original.sh` script, 
with the first parameter being the output name from `make_reads.py` 
```bash
$ . curl_original.sh <output_name>
``` 

### Basecalling
Base calling was completed using ONT Albacore 2.1.3 on both generated starts reads and generated ends reads separately.  
These reads are then mapped back to a reference sequence using minimap2 with standard ONT parameters.
