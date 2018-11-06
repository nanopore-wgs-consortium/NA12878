This page contains brief information and files from the consortium analysis.
### Performance measurements
We calculated sequencing statistics using [marginStats](https://github.com/benedictpaten/marginAlign) on alignment of native RNA and cDNA reads to gencode.v27.transcripts.fa using minimap2 (_-ax map-ont_ mode). We created a summary of unique genes and isoforms detecte by native RNA sequence data upon alignments fo the GENCODE v27 reference sequence set. Additionally, we calculated 5mers in sequence data relative to FLAIR high-confidence reference isoforms. 

 - [Genes and Isoforms detected](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/Supplementary_Tables_S1_S2.Native_RNA_genes_isoforms_GENCODEv27.xlsx)
 - [Kmer counts](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/Supplementary_Tables_S3_S4.Kmer_counts_nativeRNA_cDNA.xlsx)
 
### FLAIR isoforms
We used GENCODE v24 to align the pass native RNA and pass cDNA reads.  
Isoforms defined from [FLAIR v1.1](https://github.com/BrooksLabUCSC/flair) are in [PSL format](https://genome.ucsc.edu/FAQ/FAQformat.html#format2). From the native RNA data, we generated two sets of isoforms: set A and set B. Set A contains all isoforms (71,899 isoforms) from default FLAIR output with a minimum of 5 supporting reads, as described in the Online Methods. Set B (50,039 isoforms) is a more stringent set of nvRNA isoforms than set A. To generate set B, set A isoforms that are subsets of longer set A isoforms are removed and only the longest isoform of each unique splice junction chain is retained. We also have a set of FLAIR isoforms defined from cDNA data (99,574 isoforms).

 - [nvrna.flair.isoforms.setA.psl](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/nvrna.flair.isoforms.setA.psl)
 - [nvrna.flair.isoforms.setB.psl](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/nvrna.flair.isoforms.setB.psl)
 - [cdna.flair.isoforms.psl](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/cdna.flair.isoforms.psl)
 
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
 - [Poly-A README](https://github.com/nanopore-wgs-consortium/NA12878/blob/master/nanopore-human-transcriptome/phase1_polyA_README.md)
 - [m6A README](https://github.com/nanopore-wgs-consortium/NA12878/blob/master/nanopore-human-transcriptome/phase1_m6A_README.md)


