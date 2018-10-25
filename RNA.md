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

### Native RNA (full dataset, 30 runs)

   - [Pass](http://s3.amazonaws.com/nanopore-human-wgs/rna/fastq/NA12878-DirectRNA.pass.dedup.fastq.gz), 10302647 reads, mean 1030.24, N50 1334
   - [Fail](http://s3.amazonaws.com/nanopore-human-wgs/rna/fastq/NA12878-DirectRNA.fail.dedup.fastq.gz), 2686736 reads, mean 430.96, N50 840

### 1D cDNA (full dataset, 12 runs)

   - [Pass](http://s3.amazonaws.com/nanopore-human-wgs/rna/fastq/NA12878-cDNA-1D.pass.dedup.fastq), 15152101 reads, mean 932.86, N50 1072
   - [Fail](http://s3.amazonaws.com/nanopore-human-wgs/rna/fastq/NA12878-cDNA-1D.fail.dedup.fastq), 9129338 reads, mean 661.90, N50 841

### Combined Albacore Summary

   - [Summary File (gzip)](http://s3.amazonaws.com/nanopore-human-wgs/rna/summaries/NA12878-DirectRNA-cDNA-summary.dedup.txt.gz)

## FASTQ (Sequence Data) and FAST5 (Raw Signal Data)
FASTQ and FAST5 files for the dataset (split by centre and sample) can be found [here](https://github.com/mitenjain/NA12878/blob/master/nanopore-human-transcriptome/individualRuns.md).

## Alignment Files

All alignments performed using minimap2.

| FileType | Reference | Params | BAM | BAI |
| -------- | --------- | ------ | --- | --- |
| Native RNA Pass | [hg38](ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/technical/reference/GRCh38_reference_genome/GRCh38_full_analysis_set_plus_decoy_hla.fa) | -ax splice -uf -k14 | [hg38 BAM](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-DirectRNA.pass.dedup.NoU.fastq.hg38.minimap2.sorted.bam) | [hg38 BAI](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-DirectRNA.pass.dedup.NoU.fastq.hg38.minimap2.sorted.bam.bai) | 
| Native RNA Pass | [SIRVome isoforms ERCCs 170612a.fasta](http://s3.amazonaws.com/nanopore-human-wgs/rna/referenceFastaFiles/sirv/SIRVome_isoforms_ERCCs_170612a.fasta) | -ax splice --splice-flank=no | [SIRVome BAM](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-DirectRNA.pass.dedup.NoU.fastq.SIRVome.minimap2.sorted.bam) | [SIRVome BAI](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-DirectRNA.pass.dedup.NoU.fastq.SIRVome.minimap2.sorted.bam.bai) |
| Native RNA Fail | [hg38](ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/technical/reference/GRCh38_reference_genome/GRCh38_full_analysis_set_plus_decoy_hla.fa) | -ax splice -uf -k14 | [hg38 BAM](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-DirectRNA.fail.dedup.NoU.fastq.hg38.minimap2.sorted.bam) | [hg38 BAI](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-DirectRNA.fail.dedup.NoU.fastq.hg38.minimap2.sorted.bam.bai) |
| Native RNA Fail | [SIRVome isoforms ERCCs 170612a.fasta](http://s3.amazonaws.com/nanopore-human-wgs/rna/referenceFastaFiles/sirv/SIRVome_isoforms_ERCCs_170612a.fasta) | -ax splice --splice-flank=no | [SIRVome BAM](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-DirectRNA.fail.dedup.NoU.fastq.SIRVome.minimap2.sorted.bam) | [SIRVome BAI](http://s3.amazonaws.com/nanopore-human-wgs/rna/bamFiles/NA12878-DirectRNA.fail.dedup.NoU.fastq.SIRVome.minimap2.sorted.bam.bai) |


## Reference Files

### GRCh38
GRCh38 and BWA indices used can be downloaded from the pre-computed 1000 genomes GRCh38 BWA database at ftp://ftp-trace.ncbi.nih.gov/1000genomes/ftp/technical/reference/GRCh38_reference_genome/ (with decoys)

### SIRVome

   - [SIRVome isoforms ERCCs 170612a.fasta](http://s3.amazonaws.com/nanopore-human-wgs/rna/referenceFastaFiles/sirv/SIRVome_isoforms_ERCCs_170612a.fasta)
   - [SIRVome isoforms ERCCs Lot001485 C 170612a.gtf](http://s3.amazonaws.com/nanopore-human-wgs/rna/referenceFastaFiles/sirv/SIRVome_isoforms_ERCCs_Lot001485_C_170612a.gtf)
   - [SIRVome isoforms ERCCs Lot001485 I 170612a.gtf](http://s3.amazonaws.com/nanopore-human-wgs/rna/referenceFastaFiles/sirv/SIRVome_isoforms_ERCCs_Lot001485_I_170612a.gtf)
   - [SIRVome isoforms ERCCs Lot001485 O 170612a.gtf](http://s3.amazonaws.com/nanopore-human-wgs/rna/referenceFastaFiles/sirv/SIRVome_isoforms_ERCCs_Lot001485_O_170612a.gtf)

### GENCODE v27




## External Links

Heng Li has make a [custom track for the UCSC genome browser](http://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&position=chr6:43,767,094-43,788,458&hgct_customText=track%20type%3DbigBed%20name%3DNA12878-DirectRNA.minimap2-2.5%20useScore%3D1%20visibility%3D4%20itemRgb%3D%22On%22%20bigDataUrl%3Dhttps%3A%2F%2Ffiles.osf.io%2Fv1%2Fresources%2Fb5nm2%2Fproviders%2Fosfstorage%2F5a2347599ad5a10272ed5739%3Faction%3Ddownload%26version%3D1%26direct) from the direct RNA dataset. Thanks Heng!  [1]


## References

[1] Li, H  Twitter [link](https://twitter.com/lh3lh3/status/937166309414064129)
