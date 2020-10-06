# Subtelomere/Telomere Repeat analysis

### Identifying reads containing telomere (TTAGGG) sequence.
Ultra-long (100 kb) reads containing telomere sequences were identified using HMMER (v3.1b1,Eddy et al, 2001). Two profile HMMs were constructed from a reference telomere [TTAGGG]n sequence (Genbank M19946.1), representing the 5’-3’ orientation and reverse complement. In doing so, we determined 140 reads that contain telomere sequences.  This analysis offered a candidate list, where we expected some proportion to be false positives.

### Determine mapping to subtelomeric regions in the genome
Telomere-containing 100kb+ reads were aligned to the human reference genome (GRCh38) using minimap (Li et al, 2018; https://github.com/lh3/minimap2). Alignments converted from sam format into bed format using samtools (samtools view -bS file.sam | samtools sort - file_sorted; Li et al. 2009) and bedtools (bamToBed -ed -i file_sorted;  Quinlan and Hall, 2010).  Reads were identified as ‘subtelomeric’ that confidently mapped within 100 kb of an annotated end of a given chromosome assembly. 

### Manual characterization of telomere ends
Reads identified to be subtelomeric with telomere sequence were investigated manually to determine the region extending into the telomeric array, and the corresponding results were provided in our supplemental table, and figure 5.  In this analysis, we found that the sequences were miscalled to also represent an AAAATT repeat due to a shift in ionic current. 

Important Consideration: The length analysis did not assume that we had reached the true end of the telomere. Further, we expected to report a distribution of telomere lengths for each chromosome end rather than a single length. Therefore data presented in our paper represents the averaged length. 

### Included files
 - [tel.hmm](tel.hmm) 
 - [tel.hmmOut.txt](tel.hmmOut.txt)
 - [tel.rc.hmm](tel.rc.hmm)

## References
 - Eddy, Sean R. "HMMER: Profile hidden Markov models for biological sequence analysis." (2001).
 - Li, Heng, et al. "The sequence alignment/map format and SAMtools." Bioinformatics 25.16 (2009): 2078-2079.
 - Quinlan, Aaron R., and Ira M. Hall. "BEDTools: a flexible suite of utilities for comparing genomic features." Bioinformatics26.6 (2010): 841-842.


