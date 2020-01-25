## m6A MODIFICATION README

The following intermediate files, generated during execution of the m6A analysis are provided:    -   

 - nvrna_evalign_GGACU_dataframe.txt
Intersection of nanopolish eventalign caller output and FLAIR isoform detection output. Contains the following information as each row represents a GGACU motif within a read:
    - (1) Position: genomic position of the N⁶-Methyladenosine or Adenine
    - (2) Isoform_ID: Ensembl transcript ID or FLAIR ID read maps to
    - (3) Gene_ID: Ensembl gene ID read maps to
    - (4) Event_mean: Aligned nanopore signal events mean to GGACU motif
    - (5) Gene_symbol: Gene name

 - mod_bonferroni_stats.txt - This file contains isoform-specific statistical testing followed by bonferroni correcion:
    - (1) Position: genomic position of the N⁶-Methyladenosine or Adenine 
    - (2)  Gene ID: Ensembl transcript ID or FLAIR ID read maps to
    - (3)  Iso_1: The first isoform to analyze 
    - (4)  Iso_1_#events: Number of events for isoform 1
    - (6) Iso1_median: The median current value associated with isoform 1
    - (7)  Iso_2: The second isoform to analyze 
    - (8)  Iso_2_#events: Number of events for isoform 2
    - (9) Iso2_median: The median current value associated with isoform 2
    - (10) Pval_kruskal: p-value for Kruskal Wallis statistical test
    - (11) Pval_KS: p-value for Kolmogorov–Smirnov statistical test
    - (12) Pval_ttest: p-value for student’s t-test 
    - (13) Pval_kruskal_corrected	: Correced p-value for Kruskal Wallis statistical test
    - (14) Pval_KS_corrected: Corrected p-value for Kolmogorov–Smirnov statistical test
    - (15) Pval_ttest_corrected: Corrected p-value for student’s t-test 
    - (16) Reject: Whether the null hypothesis is rejected (True) and two isoforms have statistically different current distributions

### Files for flair_sensitive, flair_stringent, gencode_sensitive, and gencode_stringent isoform sets

 | Isoform set | Dataframe | Stats bonferroni |
 | ----------- | --------- | ---------------- | 
 | flair_sensitive | [nvrna_evalign_GGACU_dataframe_sensitive.txt](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase2_analyses/nvrna_evalign_GGACU_dataframe_sensitive.txt) | [flair_sensitive_mod_stats_bonferroni.txt](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase2_analyses/flair_sensitive_mod_stats_bonferroni.txt) |
 | flair_stringent | [nvrna_evalign_GGACU_dataframe_stringent.txt](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase2_analyses/nvrna_evalign_GGACU_dataframe_stringent.txt) | [flair_stringent_mod_stats_bonferroni.txt](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase2_analyses/flair_stringent_mod_stats_bonferroni.txt) |
 | gencode_sensitive | [nvrna_evalign_GGACU_dataframe_gencode_sensitive.txt](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase2_analyses/nvrna_evalign_GGACU_dataframe_gencode_sensitive.txt) | [gencode_sensitive_mod_stats_bonferroni.txt](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase2_analyses/gencode_sensitive_mod_stats_bonferroni.txt) |
 | gencode_stringent | [nvrna_evalign_GGACU_dataframe_gencode_stringent.txt](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase2_analyses/nvrna_evalign_GGACU_dataframe_gencode_stringent.txt) | [gencode_stringent_mod_stats_bonferroni.txt](http://s3.amazonaws.com/nanopore-human-wgs/rna/phase2_analyses/gencode_stringent_mod_stats_bonferroni.txt) |

