#!/usr/bin/env RnvRNAipt

library(calibrate)
args <- commandArgs(trailingOnly = T)

cDNA <- read.delim(args[1], header=1)
nvRNA <- read.delim(args[2], header=1)

pdf(args[3])
library(lattice)

cDNA_cov <- as.numeric(args[4]) * 1E-6 #9540204188 Mb
RNA_cov <- as.numeric(args[5]) * 1E-6 #8856592766 Mb

# individual
plot(cDNA$readCount/cDNA_cov, cDNA$refCount/cDNA_cov, col="#ff7f0e", xlim=c(0,11E3), ylim=c(0,11E3), pch=15,  cex=1, xlab="Normalized 5-mer count in reads", ylab="5-mer count per Mb reference sequence", main="all cDNA kmers")
legend(x="bottomright", legend=c("cDNA"), col=c("#ff7f0e"),pch=c(15), cex=1)

plot(nvRNA$readCount/RNA_cov, nvRNA$refCount/RNA_cov, col="#1f77b4", xlim=c(0,11E3), ylim=c(0,11E3), pch=17, cex=1, xlab="Normalized 5-mer count in reads", ylab="5-mer count per Mb reference sequence", main="all RNA kmers")
legend(x="bottomright", legend=c("RNA"), col=c("#1f77b4"),pch=c(17), cex=1)

# together
plot(cDNA$readCount/cDNA_cov, cDNA$refCount/cDNA_cov, col="#ff7f0e", xlim=c(0,11E3), ylim=c(0,11E3), pch=15, cex=1, xlab="", ylab="")
par(new=TRUE)
plot(nvRNA$readCount/RNA_cov, nvRNA$refCount/RNA_cov, col="#1f77b4", xlim=c(0,11E3), ylim=c(0,11E3), pch=17, cex=1, xlab="Normalized 5-mer count in reads", ylab="5-mer count per Mb reference sequence", main="all kmers")
legend(x="bottomright", legend=c("cDNA", "RNA"), col=c("#ff7f0e", "#1f77b4"),pch=c(15,17), cex=1)

# without TTTTT
plot(cDNA$readCount/cDNA_cov, cDNA$refCount/cDNA_cov, col="#ff7f0e", xlim=c(0,6.5E3), ylim=c(0,6.5E3), pch=15, cex=1, xlab="", ylab="")
par(new=TRUE)
plot(nvRNA$readCount/RNA_cov, nvRNA$refCount/RNA_cov, col="#1f77b4", xlim=c(0,6.5E3), ylim=c(0,6.5E3), pch=17, cex=1, xlab="Normalized 5-mer count in reads", ylab="5-mer count per Mb reference sequence", main="kmers without cDNA TTTTT")
legend(x="bottomright", legend=c("cDNA", "RNA"), col=c("#ff7f0e", "#1f77b4"),pch=c(15,17), cex=1)

# without TTTTT and AAAAA
plot(cDNA$readCount/cDNA_cov, cDNA$refCount/cDNA_cov, col="#ff7f0e", xlim=c(0,4E3), ylim=c(0,4E3), pch=15, cex=1, xlab="", ylab="")
par(new=TRUE)
plot(nvRNA$readCount/RNA_cov, nvRNA$refCount/RNA_cov, col="#1f77b4", xlim=c(0,4E3), ylim=c(0,4E3), pch=17, cex=1, xlab="Normalized 5-mer count in reads", ylab="5-mer count per Mb reference sequence", main="kmers without cDNA TTTTT and cDNA AAAAA")
legend(x="bottomright", legend=c("cDNA", "RNA"), col=c("#ff7f0e", "#1f77b4"),pch=c(15,17), cex=1)


dev.off()
