# Whole Human Genome Sequencing Project

## Introduction

We have sequenced the CEPH1463 (NA12878/GM12878, Ceph/Utah pedigree) human genome reference standard on the Oxford Nanopore MinION using 1D ligation kits (450 bp/s) using R9.4 chemistry (FLO-MIN106).

Human genomic DNA from GM12878 human cell line (Ceph/Utah pedigree) was either purchased from Coriell - "DNA" - (cat no NA12878) or extracted from the cultured cell line - "cells".  As the DNA is native, modified bases will be preserved.

# Data reuse and license

We encourage the reuse of this data in your own analysis and publications which is released under the Creative Commons CC-BY license. Therefore we would be grateful if you would cite the reference below if you do.

# Citation

Miten Jain, Sergey Koren, Karen H Miga, Josh Quick, Arthur C Rand, Thomas A Sasani, John R Tyson, Andrew D Beggs, Alexander T Dilthey, Ian T Fiddes, Sunir Malla, Hannah Marriott, Tom Nieto, Justin O'Grady, Hugh E Olsen, Brent S Pedersen, Arang Rhie, Hollian Richardson, Aaron R Quinlan, Terrance P Snutch, Louise Tee, Benedict Paten, Adam M Phillippy, Jared T Simpson, Nicholas J Loman & Matthew Loose. Nanopore sequencing and assembly of a human genome with ultra-long reads. Nature Biotechnology doi: <a href="https://doi.org/10.1038/nbt.4060">doi:10.1038/nbt.4060</a>.

# Preprint

Miten Jain, Sergey Koren, Josh Quick, Arthur C Rand, Thomas A Sasani, John R Tyson, Andrew D Beggs, Alexander T Dilthey, Ian T Fiddes, Sunir Malla, Hannah Marriott, Karen H Miga, Tom Nieto, Justin O'Grady, Hugh E Olsen, Brent S Pedersen, Arang Rhie, Hollian Richardson, Aaron Quinlan, Terrance P Snutch, Louise Tee, Benedict Paten, Adam M. Phillippy, Jared T Simpson, Nicholas James Loman, Matthew Loose. Nanopore sequencing and assembly of a human genome with ultra-long reads. bioRxiv. doi: <a href="https://doi.org/10.1101/128835">https://doi.org/10.1101/128835</a>.


# rel5 (genomic DNA)

rel5 is a merger of NA12878 DNA sequencing data from rel3 (regular sequencing protocols) and rel4 (ultra-read set), recalled with the latest generation callers (Albacore 2.1 and guppy 0.3).

## Notes on chunk size

Mike Schatz (Johns Hopkins) and Fritz Sedlazeck (CSHL) noticed that the Albacore 2.1 had a high frequency of long false positive deletions that were confounding SV prediction.  This was tracked down with the help of Chris Wright and Tim Massingham at ONT to the "chunk size" setting and the computation of signal scaling. Changing this value to 10000 should remove this problem and was performed for the Guppy calls.


## Reference

GRCh38 with decoys was used as the reference file: [GRCh38_full_analysis_set_plus_decoy_hla.fa](http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/GRCh38_reference_genome/GRCh38_full_analysis_set_plus_decoy_hla.fa).


## Guppy

Data was downloaded from the ENA raw submission. Guppy was run on the GridION X5. Calling took approximately 48 hours on dual GPUs (1080 Ti), therefore basecalling speed was ~2.4Gb/hour.

### Downloads

   - <a href="https://s3.amazonaws.com/nanopore-human-wgs/rel5-guppy-0.3.0-chunk10k.fastq.gz">Guppy 0.3 gDNA dataset (10kb chunk size)</a>

Minimap2 alignments (``minimap2 -t 12 -ax map-ont -L GRCh38_full_analysis_set_plus_decoy_hla.fa``) and samtools 1.6 with new -L flag:

   - <a href="https://s3.amazonaws.com/nanopore-human-wgs/rel5-guppy-0.3.0-chunk10k.sorted.bam">BAM</a>, <a href="https://s3.amazonaws.com/nanopore-human-wgs/rel5-guppy-0.3.0-chunk10k.sorted.bam.bai">BAI</a>

## Albacore 2.1

These basecalls are not recommended due to the above mentioned chunk size problem, but are
included for completeness.

### Downloads

   - <a href="http://s3.amazonaws.com/NA12878-Albacore2.1.fastq.gz">Albacore 2.1</a>

Minimap2 alignments (``minimap2 -t 12 -ax map-ont -L GRCh38_full_analysis_set_plus_decoy_hla.fa``):

   - <a href="http://s3.amazonaws.com/nanopore-human-wgs/NA12878-Albacore2.1.sorted.bam">BAM</a>, <a href="http://s3.amazonaws.com/nanopore-human-wgs/NA12878-Albacore2.1.sorted.bam.bai">BAI</a>.

## Assembly

Adam Phillippy and Sergey Koren have posted a new [Canu 1.7 + WTDBG + Nanopolish](https://gembox.cbcb.umd.edu/triobinning/albacore_canu_wtdbg_nanopolish2.fasta) assembly using a dataset equivalent to the Albacore 2.1 reads above over on their [blog](https://genomeinformatics.github.io/na12878update/).

## Previous versions
For previous versions of data (rel3 and rel4), please go to: (nanopore-human-genome/rel_3_4.md)

# Acknowledgements

We would like to acknowledge the support of Oxford Nanopore Technologies in generating this dataset, with particular thanks to Rosemary Dokos, Oliver Hartwell, Jonathan Pugh and Clive Brown. We would like to thank Radoslaw Poplawski and Simon Thompson for technical assistance with configuration and optimising of the CLIMB platform file system. We are grateful to Angel Pizarro and Jed Sundwall at Amazon Web Services for hosting this dataset as an <a href="https://aws.amazon.com/government-education/open-data/">AWS Open Data</a> set.

