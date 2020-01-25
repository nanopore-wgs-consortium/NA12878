# Phase 2 analyses

This page contains updated information and files from the consortium analysis included in the manuscript published in [Nature Methods](https://www.nature.com/articles/s41592-019-0617-2).

### Performance measurements
We calculated sequencing statistics using [marginStats](https://github.com/benedictpaten/marginAlign) on alignment of native RNA and cDNA reads to gencode.v27.transcripts.fa using minimap2 (_-ax map-ont_ mode). We created a summary of unique genes and isoforms detecte by native RNA sequence data upon alignments fo the GENCODE v27 reference sequence set. Additionally, we calculated 5mers in sequence data relative to FLAIR high-confidence reference isoforms. 

 - [Genes and Isoforms detected](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/Supplementary_Tables_S1_S2.Native_RNA_genes_isoforms_GENCODEv27.xlsx)
 - [Kmer counts](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/Supplementary_Tables_S3_S4.Kmer_counts_nativeRNA_cDNA.xlsx)
 
### FLAIR isoforms
The [FLAIR](https://github.com/BrooksLabUCSC/flair) isoforms are in [PSL](https://genome.ucsc.edu/FAQ/FAQformat.html#format2) format. We have provided tab-delimited files that specify the names of all the reads (column 1) and the corresponding [GENCODE v27 isoforms](https://www.gencodegenes.org/human/release_27.html) for each read (column 2). We used the native RNA reads with Lab 6 reads removed to generate these isoform sets. The "sensitive" sets retain the isoforms that follow the  criterion that each isoform has a minimum of three supporting reads, with each supporting read mapping with MAPQ>0. Isoforms are filtered out from these sets to generate the "stringent" sets. The "stringent" criteria maintain that the isoform should have a minimum of 3 supporting reads that span >= 80% of the isoform and a minimum of 25 nt into the first and last exons.

 - [nvrna.190415.190419.isoforms.stringent.21columns.queryfixed.psl](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase2_analyses/nvrna.190415.190419.isoforms.stringent.21columns.queryfixed.psl)
 - [nvrna.190415.isoforms.sensitive.21columns.queryfixed.psl](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase2_analyses/nvrna.190415.isoforms.sensitive.21columns.queryfixed.psl)
 - [gencode.v27.nobham.nvrna.mapont.q1.map.txt](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase2_analyses/gencode.v27.nobham.nvrna.mapont.q1.map.txt)
 - [gencode.v27.nobham.nvrna.mapont.q1.stringent.map.190420.190421.txt](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase2_analyses/gencode.v27.nobham.nvrna.mapont.q1.stringent.map.190420.190421.txt)
 
### Poly(A) calls

 - [poly-A all](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/NA12878_DirectRNA_polyA_all.txt)
 - [poly-A primary](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/NA12878_DirectRNA_polyA_primary.txt)
 - A reproducible pipeline for generating all poly(A) calls from the fast5 data associated to the Oxford Nanopore RNA standards is available [at this repository](https://github.com/paultsw/polya_analysis).

### Nanopolish indexes for signal analyses
In order to create indexing files to run [nanopolish](https://github.com/jts/nanopolish) eventalign, then to parse out our alignments by kmer position and associate ionic current information, we used the following commands:

	nanopolish index -d /path/to/raw_fast5s/ -s sequencing_summary.txt reads.fastq
	nanopolish eventalign --scale-events -n -t 8 --reads reads.fastq --bam reads.bam --genome GRCh38.fasta

Here is the zip file containing [nanopolish](https://github.com/jts/nanopolish) indexes for the native RNA and IVT RNA data. These were used for ionic current-level analyses of m6A and inosine modifications. Once downloaded, edit the paths appropriately for your usage.

 - [Nanopolish Indexes](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/rnaconsort.npolish.idx.zip)

### Haplotyping stats

 - [Haplotyping stats](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/Supplementary_Tables_S5.HaplotypingStatsBinom_HEADER_181030.txt)

### Allele-specific expression

 - [Genes with allele-specific isoforms](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/Supplementary_Tables_S6.GenesWithAlleleSpecificIsoformsTEXT.txt)

### Detailed poly-A and m6A README
 - [Poly-A README](phase1_polyA_README.md)
 - [m6A README](phase1_m6A_README.md)


