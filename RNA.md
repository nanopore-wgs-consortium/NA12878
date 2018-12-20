# Direct RNA and cDNA Sequencing of a human transcriptome on Oxford Nanopore MinION and GridION

## Introduction

We have sequenced the CEPH1463 (NA12878/GM12878, Ceph/Utah pedigree) human genome reference standard on the Oxford Nanopore MinION using direct RNA sequencing kits (30 flowcells) and using the 1D ligation kit (SQK-LSK108) on R9.4 flowcells using R9.4 chemistry (FLO-MIN106). RNA from the GM12878 human cell line (Ceph/Utah pedigree) was extracted from the cultured cell line.

## Contributors

 - Nick Loman, Josh Quick, Andrew Beggs, Jaqueline Goes de Jesus (_University of Birmingham_)
 - Matt Loose, Nadine Holmes, Matthew Carlile (_University of Nottingham_)
 - Winston Timp, Roham Razaghi, Timothy Gilpatrick, Norah Sadowski, Rachael E. Workman (_JHU_)
 - Jared Simpson, Phil Zuzarte, Paul Tang (_OICR_)
 - Terry Snutch, John Tyson (_UBC_)
 - Mark Akeson, Angela N. Brooks, Hugh E. Olsen, Benedict Paten, Alison Tang, Miten Jain (_UCSC_)

## Acknowledgements

We are most grateful to Daniel Garalde, Daniel Jachimowicz, Andy Heron, Rosemary Dokos at Oxford Nanopore Technologies for technical and logistical assistance.

## Basecalls (Albacore 2.1)
Full Native RNA dataset (30 runs) and full cDNA dataset (12 runs). 

| FileType | # runs | # reads | Mean (b) | Read N50 (b) | Link |
| -------- | ------ | ------- | -------- | ------------ | ---- |
| Native RNA Pass | 30 | 10302647 | 1030.24 | 1334 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rna/fastq/NA12878-DirectRNA.pass.dedup.fastq.gz) | 
| Native RNA Fail | 30 | 2686736 | 430.96 | 840 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rna/fastq/NA12878-DirectRNA.fail.dedup.fastq.gz) | 
| | | | | | |
| cDNA Pass | 12 | 15152101 | 932.86 | 1072 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rna/fastq/NA12878-cDNA-1D.pass.dedup.fastq) | 
| cDNA Fail | 12 | 9129338 | 661.90 | 841 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rna/fastq/NA12878-cDNA-1D.fail.dedup.fastq) | 

### Combined Albacore Summary

   - [Summary File (gzip)](http://s3.amazonaws.com/nanopore-human-wgs/rna/summaries/NA12878-DirectRNA-cDNA-summary.dedup.txt.gz)

### FASTQ (Sequence Data), FAST5 (Raw Signal Data), and Bulk FAST5 (Continuous Data)
FASTQ and FAST5 files for the dataset (split by centre and sample) can be found [here](nanopore-human-transcriptome/fastq_fast5_bulk.md). The continous Bulk FAST5 files could be visualized using [bulkvis](https://github.com/LooseLab/bulkvis).

## Alignment Files

All alignments performed using [minimap2](https://github.com/lh3/minimap2).

| FileType | Reference | Params | BAM | BAI |
| -------- | --------- | ------ | --- | --- |
| Native RNA Pass | GRCh38_full_analysis_set_plus_decoy_hla.fa | -ax splice -uf -k14 | [hg38 BAM](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-DirectRNA.pass.dedup.NoU.fastq.hg38.minimap2.sorted.bam) | [hg38 BAI](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-DirectRNA.pass.dedup.NoU.fastq.hg38.minimap2.sorted.bam.bai) | 
| Native RNA Pass | SIRVome_isoforms_ERCCs_170612a.fasta | -ax splice --splice-flank=no | [SIRVome BAM](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-DirectRNA.pass.dedup.NoU.fastq.SIRVome.minimap2.sorted.bam) | [SIRVome BAI](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-DirectRNA.pass.dedup.NoU.fastq.SIRVome.minimap2.sorted.bam.bai) |
| Native RNA Fail | GRCh38_full_analysis_set_plus_decoy_hla.fa | -ax splice -uf -k14 | [hg38 BAM](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-DirectRNA.fail.dedup.NoU.fastq.hg38.minimap2.sorted.bam) | [hg38 BAI](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-DirectRNA.fail.dedup.NoU.fastq.hg38.minimap2.sorted.bam.bai) |
| Native RNA Fail | SIRVome_isoforms_ERCCs_170612a.fasta | -ax splice --splice-flank=no | [SIRVome BAM](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-DirectRNA.fail.dedup.NoU.fastq.SIRVome.minimap2.sorted.bam) | [SIRVome BAI](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-DirectRNA.fail.dedup.NoU.fastq.SIRVome.minimap2.sorted.bam.bai) |
| | | | | |
| cDNA Pass | GRCh38_full_analysis_set_plus_decoy_hla.fa | -ax splice -uf -k14 | [hg38 BAM](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-cDNA-1D.pass.dedup.fastq.hg38.minimap2.sorted.bam) | [hg38 BAI](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-cDNA-1D.pass.dedup.fastq.hg38.minimap2.sorted.bam.bai) | 
| cDNA Pass | SIRVome_isoforms_ERCCs_170612a.fasta | -ax splice --splice-flank=no | [SIRVome BAM](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-cDNA-1D.pass.dedup.fastq.SIRVome.minimap2.sorted.bam) | [SIRVome BAI](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-cDNA-1D.pass.dedup.fastq.SIRVome.minimap2.sorted.bam.bai) |
| cDNA Fail | GRCh38_full_analysis_set_plus_decoy_hla.fa | -ax splice -uf -k14 | [hg38 BAM](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-cDNA-1D.fail.dedup.fastq.hg38.minimap2.sorted.bam) | [hg38 BAI](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-cDNA-1D.fail.dedup.fastq.hg38.minimap2.sorted.bam.bai) |
| cDNA Fail | SIRVome_isoforms_ERCCs_170612a.fasta | -ax splice --splice-flank=no | [SIRVome BAM](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-cDNA-1D.fail.dedup.fastq.SIRVome.minimap2.sorted.bam) | [SIRVome BAI](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-cDNA-1D.fail.dedup.fastq.SIRVome.minimap2.sorted.bam.bai) |


## Analyses 
Various analyses from the consortium work and the associated files can be found [here](nanopore-human-transcriptome/phase1_analyses.md).


## Reference Files

Details on the reference files used for analyses, and their download links can be found [here](nanopore-human-transcriptome/reference.md)

## External Links

Heng Li has make a [custom track for the UCSC genome browser](http://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&position=chr6:43,767,094-43,788,458&hgct_customText=track%20type%3DbigBed%20name%3DNA12878-DirectRNA.minimap2-2.5%20useScore%3D1%20visibility%3D4%20itemRgb%3D%22On%22%20bigDataUrl%3Dhttps%3A%2F%2Ffiles.osf.io%2Fv1%2Fresources%2Fb5nm2%2Fproviders%2Fosfstorage%2F5a2347599ad5a10272ed5739%3Faction%3Ddownload%26version%3D1%26direct) from the direct RNA dataset. Thanks Heng!  [1]


## References

[1] Li, H  Twitter [link](https://twitter.com/lh3lh3/status/937166309414064129)
