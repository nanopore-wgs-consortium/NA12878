# Oxford Nanopore Human Reference Datasets

## Quick Links

  * [Genomic DNA project](blob/master/Genome.md)

  * [RNA project](blob/master/RNA.md)

## Data availability

### Notes on downloading files.

Files are generously hosted by Amazon Web Services. Although available as straight-forward HTTP links, download performance is improved by using the Amazon Web Services <a href="https://aws.amazon.com/cli/">command-line interface</a>. References should be amended to use the `s3://` addressing scheme, i.e. replace `http://s3.amazon.com/nanopore-human-wgs/` with `s3://nanopore-human-wgs` to download. For example, to download `rel3-nanopore-wgs-288418386-FAB39088` to the current working directory use the following command.

    aws s3 cp s3://nanopore-human-wgs/rel3-nanopore-wgs-288418386-FAB39088.fastq.gz .

Amending the `max_concurrent_requests` etc. settings as per <a href="http://docs.aws.amazon.com/cli/latest/topic/s3-config.html">this guide</a> will improve download performance further.

# Contact

Please raise issues on this Github repository concerning this dataset.

# History

    * rel1: 1st December 2016. Initial release.
    * rel2: 5th December 2016. 25 flowcells, 58958035887 bases, 9053909 reads
    * rel3: 39 flowcells, 91240120433 bases, 14183584 reads
    * rel4: added additional 14 flowcells, 23140190547 bases, 1415868 reads
    * RNA release: 30th November 2016. 30 flowcells (direct RNA), 12 flowcells (1D cDNA)

    
