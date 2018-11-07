## m6A MODIFICATION README 


 - [nvrna_evalign_GGACU_dataframe.txt (858M)](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/nvrna_evalign_GGACU_dataframe.txt)
Intersection of nanopolish eventalign caller output and FLAIR isoform detection output. Contains the following information as each row represents a GGACU motif within a read:
	(1) Position: genomic position of the N⁶-Methyladenosine or Adenine 
        (2) Isoform_ID: Ensembl transcript ID or FLAIR ID read maps to
	(3) Gene_ID: Ensembl gene ID read maps to
	(4) Event_mean: Aligned nanopore signal events mean to GGACU motif
	(5) Gene_symbol: Gene name

 - [nvrna_evalign_GGACU_stats.txt (23M)](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/nvrna_evalign_GGACU_stats.txt)
This file contains statistics for each genomic position of GGACU motif event mean distribution:
	(1) Position: genomic position of the N⁶-Methyladenosine or Adenine 
(2) Isoform_ID: Ensembl transcript ID or FLAIR ID 
	(3) Gene_ID: Ensembl gene ID
	(4) Reads: Number of reads
	(5) Mean: Average of the Event_mean distribution 
	(6) Median: Median of the Event_mean distribution
	(7) SD: Standard Deviation of the Event_mean distribution
	(8) Distance: Difference between the Mean of the distribution and the pore model mean (123.8 pA)
	(9) Gene_symbol: Gene name

 - [EEF2_events.txt (519K)](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/EEF2_events.txt)
This file contain the distribution of Modified and Unmodified Event mean levels for nvRNA and Oligo dataset:
	(1) state: Either being Modified or Unmodified for GGACU motif
	(2) event_mean: Event mean level 
	(3) dataset: Either nvRNA or Oligo

 - [nvrna_isoforms_mod_3_threshold.txt (17K)](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase1_analyses/nvrna_isoforms_mod_3_threshold.txt)
This file contains the difference in average current levels between different gene isoforms for GGACU k-mers:
	(1) Position: genomic position of the N⁶-Methyladenosine or Adenine 
	(2) Gene: Gene name
(3) Iso_1: Ensembl transcript ID or FLAIR ID reads map to
	(4) Iso1_reads: Number of reads
	(5) Iso_2: Ensembl transcript ID or FLAIR ID reads map to
	(6) Iso2_reads: Number of reads
	(7) Diff: Difference in Event_mean distribution between the two isoforms (Iso_1 and Iso_2)



