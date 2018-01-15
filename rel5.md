# rel5 (genomic DNA)


## Introduction

rel5 is a merger of rel3 (regular sequencing protocols) and rel4 (ultra-read set), recalled with 
the latest generation callers (Albacore 2.1 and guppy 0.3).

Mike Schatz and Fritz Sedlezeck (Johns Hopkins) noticed that the Albacore 2.1 had a
high frequency of long false positive deletions that were confounding SV prediction.
This was tracked down with the help of Chris Wright and Tim Massingham at ONT to the
'chunk size' setting and the computation of signal scaling. Changing this value to 10000
should remove this problem and was performed for the Guppy calls.

## Guppy

Data was downloaded from the ENA raw submission. Guppy was run on the GridION X5. Calling took
approximately 48 hours on dual GPUs (1080 Ti), therefore basecalling speed was ~2.4Gb/hour.

### Downloads

   - <a href="https://s3.amazonaws.com/nanopore-human-wgs/rel5-guppy-0.3.0-chunk10k.fastq.gz">Guppy 0.3 gDNA dataset (10kb chunk size)</a>

## Albacore 2.1

These basecalls are not recommended due to the above mentioned chunk size problem, but are
included for completeness.

### Downloads

   - <a href="http://s3.amazonaws.com/NA12878-Albacore2.1.fastq.gz">Albacore 2.1</a>

Minimap2 alignments (``minimap2 -t 12 -ax map-ont -L GRCh38_full_analysis_set_plus_decoy_hla.fa``):

   - <a href="http://s3.amazonaws.com/nanopore-human-wgs/NA12878-Albacore2.1.sorted.bam">BAM</a>, <a href="http://s3.amazonaws.com/nanopore-human-wgs/NA12878-Albacore2.1.sorted.bam.bai">BAI</a>.


