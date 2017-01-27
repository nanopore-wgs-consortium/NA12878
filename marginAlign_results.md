# MarginAlign BAMs
`marginAlign` is a probabilistic aligner that uses an input _guide_ alignment as a starting point then realignes the
bases with a hidden Markov model (HMM). The HMM is trained using expectation maximization. The resulting alignments are
typically more accurate.

### Chained BAMs
By default `marginAlign` chains the guide alignment so that each read has one maximal (by length) alignment to the
reference.

| Chrom | BAM                                                                                      |
|  ---  | ---------------------------------------------------------------------------------------- |
| Chr7  | [BAM](https://s3-us-west-2.amazonaws.com/arand-minion-na12878/chr7/chr7_realigned.bam)   |
| Chr20 | [BAM](https://s3-us-west-2.amazonaws.com/arand-minion-na12878/chr20/chr20_realigned.bam) |
| Chr22 | [BAM](https://s3-us-west-2.amazonaws.com/arand-minion-na12878/chr22/chr22_realigned.bam) |

### Non-chained BAMs
These alignments were produced by learning the HMM from the guide (BWA) alignment then realigning, the chaining step was
skipped and so each read may have multiple alignments

| Chrom | BAM                                                                                             |
|  ---  | ______----------------------------------------------------------------------------------------------- |
| Chr7  | [BAM](https://s3-us-west-2.amazonaws.com/arand-minion-na12878/chr7/chr7_noChain_realigned.bam_) |
