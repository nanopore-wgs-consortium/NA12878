POLY(A)  README 

Two tab-separated text files with the final poly(A) calls for each read are provided: one using only the primary alignments for each read, and one using all alignments. 
Columns are organized with the following information: 
(1) readname: read ID
(2) contig: reference contig
(3) position: 5` start of the alignment.
(3) leader_start: starting sample indices of respective region
(4) adapter_start: starting sample indices of respective region
(5) polya_start: starting sample indices of respective region
(6) transcript_start: the starting sample indices of respective region
(7) read_rate: a proxy estimate for the rate the molecule traverses the pore, (nt/sec)
(8) polya_length: estimate of poly(A) tail length 
(9) qc_tag: a tag indicating detection of an error in the estimate

PolyA Caller - All reads
 - [poly-A all (1.4G)](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/NA12878_DirectRNA_polyA_all.txt)

PolyA Caller - Primary alignments
 - [poly-A primary (754M)](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/NA12878_DirectRNA_polyA_primary.txt)

The following intermediate files, generated during execution of the poly(A) pipeline are also provided : 


 - [nvrna_polya_dataframe.txt (326M)](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/nvrna_polya_dataframe.txt)
Intersection of nanopolish poly(A) caller output and FLAIR isoform detection output. Contains the following information per read:
	(1) Isoform_ID: Ensembl transcript ID or FLAIR ID read maps to
	(2) Gene_ID: Ensembl gene ID read maps to
	(3) PolyA_length: Poly(A) tail length
	(4) Gene_symbol: Gene name

nvrna_polya_genes_stat.txt (762K): Tab-separated variable file containing statistics for each gene poly(A) tail length distribution:
	(1) Isoform_ID: Ensembl transcript ID or FLAIR ID 
	(2) Gene_ID: Ensembl gene ID
	(3) Reads: Number of reads associated with the corresponding gene
	(4) Mean: Mean poly(A) tail length per gene
	(5) Median: Median poly(A) tail length per gene
	(6) SD: Standard deviation for the poly(A) tail length distribution per gene
	(7) Gene_symbol: Gene name


nvrna_polya_isoforms_stat.txt (4.9M): This file contains statistics for each isoform poly(A) tail length distribution:
	(1) Gene_ID: Ensembl gene ID
	(2) Reads: Number of reads associated with the corresponding isoform
	(3) Mean: Mean poly(A) tail length per isoform
	(4) Median: Median poly(A) tail length per isoform
	(5) SD: Standard deviation for the poly(A) tail length distribution per isoform
	(6) Gene_symbol: Gene name


MODIFICATION README 


nvrna_evalign_GGACU_dataframe.txt (858M): Intersection of nanopolish eventalign caller output and FLAIR isoform detection output. Contains the following information as each row represents a GGACU motif within a read:
	(1) Position: genomic position of the N⁶-Methyladenosine or Adenine 
(2) Isoform_ID: Ensembl transcript ID or FLAIR ID read maps to
	(3) Gene_ID: Ensembl gene ID read maps to
	(4) Event_mean: Aligned nanopore signal events mean to GGACU motif
	(5) Gene_symbol: Gene name

nvrna_evalign_GGACU_stats.txt (23M): This file contains statistics for each genomic position of GGACU motif event mean distribution:
	(1) Position: genomic position of the N⁶-Methyladenosine or Adenine 
(2) Isoform_ID: Ensembl transcript ID or FLAIR ID 
	(3) Gene_ID: Ensembl gene ID
	(4) Mean: Average of the Event_mean distribution 
	(5) Median: Median of the Event_mean distribution
	(6) SD: Standard Deviation of the Event_mean distribution
	(7) Distance: Difference between the Mean of the distribution and the pore model mean (123.8 pA)
	(8) Gene_symbol: Gene name

EEF2_events.txt (519K): This file contain the distribution of Modified and Unmodified Event mean levels for nvRNA and Oligo dataset:
	(1) state: Either being Modified or Unmodified for GGACU motif
	(2) event_mean: Event mean level 
	(3) dataset: Either nvRNA or Oligo


