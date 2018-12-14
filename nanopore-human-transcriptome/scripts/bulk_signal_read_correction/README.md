bulk_signal_read_correction
===========================

Table of Contents
=================
 - [bulk_signal_read_correction](#bulk_signal_read_correction)
 - [Table of Contents](#table-of-contents)
 - [event_finder.py](#event_finderpy)
 - [export.py](#exportpy)


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

