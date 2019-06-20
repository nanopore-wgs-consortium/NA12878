# Whole Human Genome Sequencing Project

## Introduction

We have sequenced the CEPH1463 (NA12878/GM12878, Ceph/Utah pedigree) human genome reference standard on the Oxford Nanopore MinION using 1D ligation kits (450 bp/s) using R9.4 chemistry (FLO-MIN106).

Human genomic DNA from GM12878 human cell line (Ceph/Utah pedigree) was either purchased from Coriell - "DNA" - (cat no NA12878) or extracted from the cultured cell line - "cells".  As the DNA is native, modified bases will be preserved.

# Data reuse and license

We encourage the reuse of this data in your own analysis and publications which is released under the Creative Commons CC-BY license. Therefore we would be grateful if you would cite the reference below if you do.

# Citation

Miten Jain, Sergey Koren, Karen H Miga, Josh Quick, Arthur C Rand, Thomas A Sasani, John R Tyson, Andrew D Beggs, Alexander T Dilthey, Ian T Fiddes, Sunir Malla, Hannah Marriott, Tom Nieto, Justin O'Grady, Hugh E Olsen, Brent S Pedersen, Arang Rhie, Hollian Richardson, Aaron R Quinlan, Terrance P Snutch, Louise Tee, Benedict Paten, Adam M Phillippy, Jared T Simpson, Nicholas J Loman & Matthew Loose. Nanopore sequencing and assembly of a human genome with ultra-long reads. Nature Biotechnology doi: <a href="https://doi.org/10.1038/nbt.4060">doi:10.1038/nbt.4060</a>.

# rel6 (genomic DNA)

Since the initial release Guppy basecalling improvements have continued as well as optimisations in file formats (the introduction of mutifast5 files ). To this end, we have updated the data set to incorporate the latest basecalling improvements as well as file formats.

Earlier releases should now be considered deprecated and not representative of the current state-of-the-art for nanopore sequencing.

We consider rel6 to be a significant update and so are also releasing these data as we did the original rel3&4 data flowcell by flowcell.

Reference assemblies from Adam Phillippy and Sergey Koren will be available shortly.

The total dataset is now:

* 53 flowcells
* 132,931,102,331 bases
* 15,666,888 reads

The multi fast5 files are 4.5 Tb in size.
 
Data were basecalled using:
 * Guppy Version: ONT Guppy basecalling software version 2.3.8+498297c
 * config file: dna_r9.4.1_450bps_flipflop.cfg
 * model file: template_r9.4.1_450bps_large_flipflop.jsn
 
 
 Note: One run (FAB23716) generated using R9 has currently failed rebasecalling.
 
## Multi Fast5 Files

For forward compatibility, the raw signal data has been repackaged into Multi fast5 files using the single_to_multi command from the ONT Fast5 API.

This has resulted in a significant decrease in file size for this collection as these files no longer contain events. Thus these tar files are now only 4.5 Tb in total. These files have not yet been compressed with Nanopore's new compression algorithms. We will provide this soon. 

To obtain the whole set of fast5 files we recommend using the aws client and obtaining all the data from s3://nanopore-human-wgs/rel6/MultiFast5Tars/
 
```bash
aws s3 cp s3://nanopore-human-wgs/rel6/MultiFast5Tars/ <<TARGET>>
```

Individual flowcells worth of Fast5 data can be downloaded below.

## Whole Dataset

FASTQ Data (gz) from the entire rel6 dataset is available here (131 Gb): [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/rel_6.fastq.gz)

A sequencing summary file for the entire dataset is available here (1.1 Gb): [Sequencing Summary](http://s3.amazonaws.com/nanopore-human-wgs/rel6/rel_6_sequencing_summary.txt.gz)

Individual Flowcells of data can be downloaded below. These are complete with sequencing summary files and guppy logs. FASTQ files are gzipped within the tar files.

The entire set of FASTQ tar data can be downloaded by using the aws client and downloading from s3://nanopore-human-wgs/rel6/FASTQTars/

```bash
aws s3 cp s3://nanopore-human-wgs/rel6/FASTQTars/ <<TARGET>>
```

 
## Rel6 Data

| flowcell_id | ASIC_id    | Links (Fastq/Fast5)                                                                                                                                                                                            | reads   | bases         | Mean   | N50     | Date       | Centre  | SampleType | Kit      | Pore |
|-------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|---------------|--------|---------|------------|---------|------------|----------|------|
| FAB23716*   | N/A        | Data Not Available                                                                                                                                                                                             | N/A     | N/A           | N/A    | N/A     | 14/07/2016 | UBC     | DNA        | Rapid    | R9   |
| FAB39088    | 288418386  | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB39088-288418386_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB39088-288418386_Multi_Fast5.tar)   | 668,016 | 3,929,822,468 | 5,883  | 11,218  | 19/09/2016 | Notts   | DNA        | Ligation | R9.4 |
| FAB39075    | 4246400039 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB39075-4246400039_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB39075-4246400039_Multi_Fast5.tar) | 477,495 | 3,014,355,946 | 6,313  | 13,297  | 20/09/2016 | UBC     | DNA        | Ligation | R9.4 |
| FAB39043    | 3709921973 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB39043-3709921973_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB39043-3709921973_Multi_Fast5.tar) | 442,132 | 2,574,202,451 | 5,822  | 11,141  | 23/09/2016 | Bham    | DNA        | Ligation | R9.4 |
| FAB42706    | 4111103328 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB42706-4111103328_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB42706-4111103328_Multi_Fast5.tar) | 431,694 | 2,434,471,643 | 5,639  | 9,708   | 12/10/2016 | UBC     | DNA        | Ligation | R9.4 |
| FAB41174    | 3976885577 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB41174-3976885577_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB41174-3976885577_Multi_Fast5.tar) | 117,140 | 739,850,920   | 6,316  | 8,010   | 13/10/2016 | Bham    | DNA        | Ligation | R9.4 |
| FAB42260    | 4177064552 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB42260-4177064552_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB42260-4177064552_Multi_Fast5.tar) | 269,507 | 1,583,530,766 | 5,876  | 10,022  | 13/10/2016 | UBC     | DNA        | Ligation | R9.4 |
| FAB42804    | 84744914   | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB42804-84744914_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB42804-84744914_Multi_Fast5.tar)     | 16,688  | 91,150,705    | 5,462  | 7,427   | 14/10/2016 | Bham    | DNA        | Ligation | R9.4 |
| FAB42316    | 216722908  | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB42316-216722908_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB42316-216722908_Multi_Fast5.tar)   | 573,736 | 4,047,383,848 | 7,054  | 8,493   | 14/10/2016 | Notts   | DNA        | Ligation | R9.4 |
| FAB42205    | 3573838535 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB42205-3573838535_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB42205-3573838535_Multi_Fast5.tar) | 318,133 | 2,076,803,569 | 6,528  | 10,955  | 14/10/2016 | Notts   | DNA        | Ligation | R9.4 |
| FAB42561    | 356443753  | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB42561-356443753_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB42561-356443753_Multi_Fast5.tar)   | 234,228 | 1,693,451,959 | 7,230  | 12,074  | 19/10/2016 | Notts   | DNA        | Ligation | R9.4 |
| FAB42473    | 4179682758 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB42473-4179682758_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB42473-4179682758_Multi_Fast5.tar) | 646,945 | 3,794,243,146 | 5,865  | 10,316  | 19/10/2016 | UBC     | DNA        | Ligation | R9.4 |
| FAB42395    | 4178605061 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB42395-4178605061_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB42395-4178605061_Multi_Fast5.tar) | 38,335  | 200,553,219   | 5,232  | 10,952  | 20/10/2016 | Norwich | DNA        | Ligation | R9.4 |
| FAB42476    | 3843483077 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB42476-3843483077_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB42476-3843483077_Multi_Fast5.tar) | 435,934 | 2,655,496,773 | 6,092  | 10,492  | 27/10/2016 | UBC     | DNA        | Ligation | R9.4 |
| FAB42451    | 4239353418 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB42451-4239353418_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB42451-4239353418_Multi_Fast5.tar) | 818,420 | 5,228,838,859 | 6,389  | 10,490  | 28/10/2016 | Notts   | DNA        | Ligation | R9.4 |
| FAB42704    | 87746129   | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB42704-87746129_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB42704-87746129_Multi_Fast5.tar)     | 276,653 | 2,015,520,974 | 7,285  | 11,804  | 28/10/2016 | UBC     | DNA        | Ligation | R9.4 |
| FAB42828    | 288548394  | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB42828-288548394_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB42828-288548394_Multi_Fast5.tar)   | 33,633  | 206,649,131   | 6,144  | 12,406  | 01/11/2016 | Norwich | DNA        | Ligation | R9.4 |
| FAB42810    | 352384898  | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB42810-352384898_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB42810-352384898_Multi_Fast5.tar)   | 322,286 | 2,433,213,020 | 7,550  | 12,796  | 02/11/2016 | Norwich | DNA        | Ligation | R9.4 |
| FAB42798    | 3306352129 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB42798-3306352129_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB42798-3306352129_Multi_Fast5.tar) | 193,679 | 1,543,052,592 | 7,967  | 13,046  | 03/11/2016 | Norwich | DNA        | Ligation | R9.4 |
| FAB45280    | 222619780  | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB45280-222619780_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB45280-222619780_Multi_Fast5.tar)   | 128,314 | 895,679,449   | 6,980  | 11,404  | 11/11/2016 | Norwich | DNA        | Ligation | R9.4 |
| FAB46664    | 288286712  | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB46664-288286712_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB46664-288286712_Multi_Fast5.tar)   | 491,945 | 2,335,386,447 | 4,747  | 8,819   | 15/11/2016 | UBC     | DNA        | Ligation | R9.4 |
| FAB46683    | 4246923067 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB46683-4246923067_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB46683-4246923067_Multi_Fast5.tar) | 72,713  | 447,658,919   | 6,157  | 12,183  | 17/11/2016 | Bham    | DNA        | Ligation | R9.4 |
| FAB45332    | 551111640  | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB45332-551111640_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB45332-551111640_Multi_Fast5.tar)   | 531,764 | 3,267,600,534 | 6,145  | 10,885  | 17/11/2016 | UBC     | DNA        | Ligation | R9.4 |
| FAB43577    | 3574887596 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB43577-3574887596_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB43577-3574887596_Multi_Fast5.tar) | 427,215 | 2,776,702,333 | 6,500  | 9,125   | 18/11/2016 | UCSC    | DNA        | Ligation | R9.4 |
| FAB44989    | 2567311907 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB44989-2567311907_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB44989-2567311907_Multi_Fast5.tar) | 558,539 | 3,962,530,064 | 7,095  | 9,747   | 18/11/2016 | UCSC    | DNA        | Ligation | R9.4 |
| FAF01169    | 4245879798 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF01169-4245879798_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF01169-4245879798_Multi_Fast5.tar) | 339,948 | 3,196,399,021 | 9,403  | 13,852  | 22/11/2016 | Bham    | Cells      | Ligation | R9.4 |
| FAF01441    | 3910073345 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF01441-3910073345_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF01441-3910073345_Multi_Fast5.tar) | 255,326 | 2,457,162,654 | 9,624  | 13,926  | 22/11/2016 | Bham    | Cells      | Ligation | R9.4 |
| FAB45277    | 86567043   | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB45277-86567043_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB45277-86567043_Multi_Fast5.tar)     | 336,653 | 3,287,605,917 | 9,766  | 14,002  | 22/11/2016 | Notts   | Cells      | Ligation | R9.4 |
| FAB45321**  | 19064779   | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB45321*-19064779_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB45321*-19064779_Multi_Fast5.tar)   | 299,306 | 2,817,977,026 | 9,415  | 13,594  | 22/11/2016 | Notts   | Cells      | Ligation | R9.4 |
| FAF01127    | 353303576  | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF01127-353303576_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF01127-353303576_Multi_Fast5.tar)   | 633,129 | 5,441,337,578 | 8,594  | 12,847  | 25/11/2016 | Bham    | Cells      | Ligation | R9.4 |
| FAF01132    | 84868110   | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF01132-84868110_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF01132-84868110_Multi_Fast5.tar)     | 719,983 | 6,269,018,010 | 8,707  | 12,999  | 25/11/2016 | Bham    | Cells      | Ligation | R9.4 |
| FAB49712    | 622291475  | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB49712-622291475_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB49712-622291475_Multi_Fast5.tar)   | 632,305 | 5,376,464,744 | 8,503  | 12,540  | 28/11/2016 | Bham    | Cells      | Ligation | R9.4 |
| FAF01253    | 83756522   | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF01253-83756522_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF01253-83756522_Multi_Fast5.tar)     | 471,792 | 4,034,085,735 | 8,551  | 12,561  | 28/11/2016 | Bham    | Cells      | Ligation | R9.4 |
| FAB45321**  | 285174896  | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB45321*-285174896_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB45321*-285174896_Multi_Fast5.tar) | 123,061 | 1,123,014,497 | 9,126  | 12,703  | 28/11/2016 | Notts   | Cells      | Ligation | R9.4 |
| FAB49914    | 3775529215 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB49914-3775529215_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB49914-3775529215_Multi_Fast5.tar) | 309,335 | 3,066,878,031 | 9,914  | 14,027  | 28/11/2016 | Notts   | Cells      | Ligation | R9.4 |
| FAB45271    | 152889212  | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB45271-152889212_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB45271-152889212_Multi_Fast5.tar)   | 467,701 | 3,959,651,805 | 8,466  | 12,564  | 28/11/2016 | Notts   | Cells      | Ligation | R9.4 |
| FAB49164    | 4045668814 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB49164-4045668814_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB49164-4045668814_Multi_Fast5.tar) | 747,060 | 4,997,920,867 | 6,690  | 9,366   | 06/12/2016 | UCSC    | DNA        | Ligation | R9.4 |
| FAB49908    | 481119249  | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAB49908-481119249_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAB49908-481119249_Multi_Fast5.tar)   | 227,767 | 4,416,647,293 | 19,391 | 41,839  | 09/12/2016 | Bham    | Cells      | Rapid    | R9.4 |
| FAF04090    | 3842965088 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF04090-3842965088_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF04090-3842965088_Multi_Fast5.tar) | 94,833  | 2,337,803,872 | 24,652 | 85,013  | 09/12/2016 | Bham    | Cells      | Rapid    | R9.4 |
| FAF15665    | 16056159   | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF15665-16056159_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF15665-16056159_Multi_Fast5.tar)     | 83,299  | 2,160,064,589 | 25,931 | 105,528 | 10/03/2017 | Notts   | Cells      | Ultra    | R9.4 |
| FAF13748    | 17958431   | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF13748-17958431_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF13748-17958431_Multi_Fast5.tar)     | 55,051  | 1,427,000,374 | 25,921 | 75,193  | 10/03/2017 | Notts   | Cells      | Ultra    | R9.4 |
| FAF10039    | 2901545329 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF10039-2901545329_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF10039-2901545329_Multi_Fast5.tar) | 43,709  | 1,074,279,009 | 24,578 | 60,128  | 01/03/2017 | Bham    | Cells      | Ultra    | R9.4 |
| FAF09968    | 3439856925 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF09968-3439856925_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF09968-3439856925_Multi_Fast5.tar) | 21,947  | 658,551,981   | 30,006 | 125,607 | 03/03/2017 | Bham    | Cells      | Ultra    | R9.4 |
| FAF09277    | 3709819546 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF09277-3709819546_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF09277-3709819546_Multi_Fast5.tar) | 78,080  | 2,237,071,487 | 28,651 | 118,062 | 03/06/2017 | Bham    | Cells      | Ultra    | R9.4 |
| FAF14035    | 3976726082 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF14035-3976726082_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF14035-3976726082_Multi_Fast5.tar) | 101,222 | 2,082,960,600 | 20,578 | 88,613  | 08/03/2017 | Notts   | Cells      | Ultra    | R9.4 |
| FAF15694    | 4109802543 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF15694-4109802543_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF15694-4109802543_Multi_Fast5.tar) | 63,850  | 1,743,301,488 | 27,303 | 103,541 | 06/03/2017 | Bham    | Cells      | Ultra    | R9.4 |
| FAF09713    | 4111860526 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF09713-4111860526_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF09713-4111860526_Multi_Fast5.tar) | 67,968  | 1,842,932,107 | 27,114 | 93,737  | 07/03/2017 | Bham    | Cells      | Ultra    | R9.4 |
| FAF18554    | 4178920553 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF18554-4178920553_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF18554-4178920553_Multi_Fast5.tar) | 272,029 | 3,008,840,150 | 11,060 | 25,583  | 06/03/2017 | UBC     | Cells      | Rapid    | R9.4 |
| FAF15630    | 4244782843 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF15630-4244782843_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF15630-4244782843_Multi_Fast5.tar) | 13,406  | 354,563,221   | 26,448 | 107,403 | 09/03/2017 | Notts   | Cells      | Ultra    | R9.4 |
| FAF09640    | 4245291640 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF09640-4245291640_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF09640-4245291640_Multi_Fast5.tar) | 77,481  | 1,729,363,584 | 22,319 | 89,354  | 07/03/2017 | Bham    | Cells      | Ultra    | R9.4 |
| FAF09701    | 4249180049 | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF09701-4249180049_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF09701-4249180049_Multi_Fast5.tar) | 71,733  | 1,998,980,799 | 27,867 | 116,126 | 03/03/2017 | Bham    | Cells      | Ultra    | R9.4 |
| FAF15586    | 82266371   | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF15586-82266371_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF15586-82266371_Multi_Fast5.tar)     | 82,411  | 1,990,923,468 | 24,158 | 116,036 | 08/03/2017 | Bham    | Cells      | Ultra    | R9.4 |
| FAF05869    | 87644245   | [FASTQ](http://s3.amazonaws.com/nanopore-human-wgs/rel6/FastQTars/FAF05869-87644245_Multi.tar)/[FAST5](http://s3.amazonaws.com/nanopore-human-wgs/rel6/Multi_Fast5_Tars/FAF05869-87644245_Multi_Fast5.tar)     | 451,359 | 3,892,152,689 | 8,623  | 14,576  | 08/03/2017 | UBC     | Cells      | Ligation | R9.4 |

\* This run on R9 chemistry failed basecalling. We are working to resolve this.  
** These two runs share the same flowcell ID through human error...

## Previous versions

For previous versions of data:  
    (rel5), please go to: [rel5](nanopore-human-genome/rel5.md)  
    (rel3 and rel4), please go to: [rel_3_4](nanopore-human-genome/rel_3_4.md)  

# Acknowledgements

We would like to acknowledge the support of Oxford Nanopore Technologies in generating this dataset, with particular thanks to Rosemary Dokos, Oliver Hartwell, Jonathan Pugh and Clive Brown. We would like to thank Radoslaw Poplawski and Simon Thompson for technical assistance with configuration and optimising of the CLIMB platform file system. We are grateful to Angel Pizarro and Jed Sundwall at Amazon Web Services for hosting this dataset as an <a href="https://aws.amazon.com/government-education/open-data/">AWS Open Data</a> set.

