library(tidyverse)
library(cowplot)
require(magick)
library(extrafont)
library(RColorBrewer)
# Figure 6A

make.joint.dataframe <- function(fns) {
  ## load inputs as dataframes:
  dataframes <- list()
  i <- 1
  for (fn in fns) {
    tmp <- read.csv(fn, sep = '\t')
    print(fn)
    dataframes[[i]] <- data.frame(dataset = factor(rep(fn, each=nrow(tmp[tmp$qc_tag == 'PASS',]))),
                                  lengths = pmin(tmp[tmp$qc_tag == 'PASS',]$polya_length, 300))
    i <- i + 1
  }
  # merge dataframes together and (automatically) return:
  do.call("rbind", dataframes)
}

## main loop: read filenames, construct a ggplot2 object,
## and save plot to file
main <- function() {
  ## load dataframes into a single DF:
  files <- c("~/Dropbox (Timp Lab)/RNA-Consortium/figure-7a/polyas/10x.polya.tsv", 
             "~/Dropbox (Timp Lab)/RNA-Consortium/figure-7a/polyas/15x.polya.tsv",
             "~/Dropbox (Timp Lab)/RNA-Consortium/figure-7a/polyas/30x.polya.tsv",
             "~/Dropbox (Timp Lab)/RNA-Consortium/figure-7a/polyas/60x.polya.tsv",
             "~/Dropbox (Timp Lab)/RNA-Consortium/figure-7a/polyas/60xN.polya.tsv",
             "~/Dropbox (Timp Lab)/RNA-Consortium/figure-7a/polyas/80x.polya.tsv",
             "~/Dropbox (Timp Lab)/RNA-Consortium/figure-7a/polyas/100x.polya.tsv"
)
  df <- make.joint.dataframe(files)
  
  ## make a violin plot of all filenames:
  max.ticks <- max(df$lengths)
  plot <- ggplot(df, aes(x=dataset, y=lengths, fill= dataset)) +
    theme_cowplot(font_size = 14, font_family = "ArialMT", line_size = 1)+
    geom_violin(trim = FALSE) +
    scale_x_discrete(name="Dataset",labels = c('10X','15X','30X','60X','60XN','80X','100X')) +
    scale_y_continuous(name="poly(A) length", limits=c(0,300)) +
    scale_fill_brewer(palette="Dark2") +
    theme(legend.position="none")
  # scale_y_continuous(name="est poly(A) length", breaks=seq(0,max.ticks,10), limits=c(0,300))
  
  ## save plot to file:
  ## TODO: optionally set size/dpi/etc.
  save_plot("~/Dropbox (Timp Lab)/Timplab_writing/Manuscripts/180700_NatureMethods_RNAConsortia/figures/polyA/figure6a.pdf", plot, base_aspect_ratio = 1.5)
  return(plot)
}

### run main function:
fig6a <- main()


# Figure 6B
polyA_df <- read.delim("/dilithium/Data/Nanopore/rna/polyA/NA12878_DirectRNA_polya_primary.txt", sep = "\t")
polyA_df <- polyA_df(,c(2,9,20))
polyA_df <- polyA_df %>%
  filter(polya_length <= 600)  %>%
  mutate(chr_type = ifelse(contig =="chrM","Mitochondrial","Nuclear"))

p_nuc_mito <- ggplot(polyA_df, aes(x = polya_length, fill= chr_type)) +
  theme_cowplot(font_size = 14, font_family = "ArialMT", line_size = 1)+
  geom_density(alpha= 0.5) +
  theme(strip.background =element_rect(fill="white")) +
  scale_fill_manual(name="",values = c("#de2d26", "#636363"),labels=c("Mitochondrial transcripts","Nuclear transcripts")) +
  theme(legend.position="top",legend.direction = "horizontal")
save_plot("~/Dropbox (Timp Lab)/Timplab_writing/Manuscripts/180700_NatureMethods_RNAConsortia/figures/polyA/figure6b.pdf", p_nuc_mito, base_aspect_ratio = 1.5)
nuc_df <- polyA_df %>%
  filter(contig != "chrM")

# p_nuc <- ggplot(nuc_df, aes(x = polya_length, fill= chr_type)) +
#   theme_cowplot(font_size = 14, font_family = "ArialMT", line_size = 1)+
#   geom_density(alpha= 0.5) +
#   theme(strip.background =element_rect(fill="white")) +
#   scale_fill_manual(name="",values = c("#636363"),labels=c("Nuclear transcripts")) +
#   theme(legend.position="top")
# save_plot("~/Dropbox (Timp Lab)/Timplab_writing/Manuscripts/180700_NatureMethods_RNAConsortia/figures/polyA/figure6b.pdf", p_nuc, base_aspect_ratio = 1.5)

# Figure 6D + supplements

polyA_flair = read.delim("/dilithium/Data/Nanopore/rna/analysis/out_to_R/polya/nvrna_polya_dataframe.txt", sep = "\t")

genes_20k <- polyA_flair %>%
  filter(PolyA_length <= 600, Gene_symbol == "ACTB" |Gene_symbol == "B2M"|Gene_symbol == "RPL7"|Gene_symbol == "RPL27A"|Gene_symbol == "RPS18")
genes_20k$Gene_symbol<-factor(genes_20k$Gene_symbol, levels=c("ACTB","B2M","RPL7","RPL27A","RPS18"))
p_genes_20k <- ggplot(genes_20k, aes(x = Gene_symbol, y= PolyA_length, fill= Gene_symbol)) +
  theme_cowplot(font_size = 14, font_family = "ArialMT", line_size = 1)+
  geom_violin(trim = FALSE,scale="width") + geom_boxplot(width = 0.2,outlier.shape = NA,fill="white") + 
  theme(strip.background =element_rect(fill="white"))+
  scale_fill_brewer(palette="Set1") +
  theme(legend.position="none")
save_plot("~/Dropbox (Timp Lab)/Timplab_writing/Manuscripts/180700_NatureMethods_RNAConsortia/figures/polyA/genes20k.pdf", p_genes_20k, base_aspect_ratio = 1.5)

genes_1k_20k <- polyA_flair %>%
  filter(PolyA_length <= 600, Gene_symbol == "DDX5" |Gene_symbol == "ATF4"|Gene_symbol == "PLAC8"|Gene_symbol == "RPL24"|Gene_symbol == "RPS24")
genes_1k_20k$Gene_symbol<-factor(genes_1k_20k$Gene_symbol, levels=c('DDX5','ATF4', 'PLAC8','RPL24','RPS24'))
p_genes_1k_20k <- ggplot(genes_1k_20k, aes(x = Gene_symbol, y= PolyA_length, fill= Gene_symbol)) +
  theme_cowplot(font_size = 14, font_family = "ArialMT", line_size = 1)+
  geom_violin(trim = FALSE,scale="width") + geom_boxplot(width = 0.2,outlier.shape = NA,fill="white") + 
  theme(strip.background =element_rect(fill="white"))+
  scale_fill_brewer(palette="Set2") +
  theme(legend.position="none") +
  scale_y_continuous(limits=c(0,700)) 
save_plot("~/Dropbox (Timp Lab)/Timplab_writing/Manuscripts/180700_NatureMethods_RNAConsortia/figures/polyA/figure6c.pdf", p_genes_1k_20k, base_aspect_ratio = 1.5)
  
genes_5_1k <- polyA_flair %>%
  filter(PolyA_length <= 600, Gene_symbol == "C1RL-AS1" |Gene_symbol == "SEC31B"|Gene_symbol == "IL15RA"|Gene_symbol == "C2orf88"|Gene_symbol == "SNHG22")
genes_5_1k$Gene_symbol<-factor(genes_5_1k$Gene_symbol, levels=c('C1RL-AS1','SEC31B', 'IL15RA','C2orf88','SNHG22'))
p_genes_5_1k <- ggplot(genes_5_1k, aes(x = Gene_symbol, y= PolyA_length, fill= Gene_symbol)) +
  theme_cowplot(font_size = 14, font_family = "ArialMT", line_size = 1)+
  geom_violin(trim = FALSE,scale="width") + geom_boxplot(width = 0.2,outlier.shape = NA,fill="white") + 
  theme(strip.background =element_rect(fill="white"))+
  scale_fill_brewer(palette="Set3") +
  theme(legend.position="none")
save_plot("~/Dropbox (Timp Lab)/Timplab_writing/Manuscripts/180700_NatureMethods_RNAConsortia/figures/polyA/genes5_1k.pdf", p_genes_5_1k, base_aspect_ratio = 1.5)

# Figure 6E

# DDX5 <- genes_1k_20k %>%
#   filter(Isoform_ID == "ENST00000225792" |Isoform_ID == "fc143144-3b0b-4824-839f-ede17c306f25"|
#            Isoform_ID == "a1181c33-cef3-4c7b-bbe4-5efce08bb71b"|Isoform_ID == "ENST00000578804"|
#            Isoform_ID == "855a2ee0-cad1-4144-a510-0c6a4e83c4ca" | Isoform_ID == "ENST00000581230")
# DDX5$Isoform_ID<-factor(DDX5$Isoform_ID, levels=c('ENST00000225792','fc143144-3b0b-4824-839f-ede17c306f25',
#                                                                 'a1181c33-cef3-4c7b-bbe4-5efce08bb71b','ENST00000578804',
#                                                                 '855a2ee0-cad1-4144-a510-0c6a4e83c4ca','ENST00000581230'))
# 
# p_ddx5 <- ggplot(DDX5, aes(x = Isoform_ID, y= PolyA_length, fill= Isoform_ID)) +
#   theme_cowplot(font_size = 14, font_family = "ArialMT", line_size = 1)+
#   geom_violin(trim = FALSE,scale="width") + geom_boxplot(width = 0.2,outlier.shape = NA,fill="white") + 
#   theme(strip.background =element_rect(fill="white"))+
#   scale_x_discrete(labels = c('Isoform 792','Isoform f25',
#                               'Isoform 71b','Isoform 804',
#                               'Isoform 4ca','Isoform 230')) +
#   scale_fill_brewer(palette="green") +
#   theme(legend.position="none")

DDX5 <- genes_1k_20k %>%
  filter(Isoform_ID == "ENST00000578804"|
           Isoform_ID == "855a2ee0-cad1-4144-a510-0c6a4e83c4ca" | Isoform_ID == "ENST00000581230")
DDX5$Isoform_ID<-factor(DDX5$Isoform_ID, levels=c('ENST00000578804',
                                                  '855a2ee0-cad1-4144-a510-0c6a4e83c4ca','ENST00000581230'))

my_greens = brewer.pal(n = 9, "Greens")[5:9]
p_ddx5 <- ggplot(DDX5, aes(x = Isoform_ID, y= PolyA_length, fill= Isoform_ID)) +
  theme_cowplot(font_size = 14, font_family = "ArialMT", line_size = 1)+
  geom_violin(trim = FALSE,scale="width") + geom_boxplot(width = 0.2,outlier.shape = NA,fill="white") + 
  theme(strip.background =element_rect(fill="white"))+
  scale_x_discrete(name="DDX5",labels = c('Isoform 804',
                              'Isoform 4ca','Isoform 230')) +
  scale_fill_manual(values = my_greens) +
  # scale_fill_brewer(palette="Greens") +
  theme(legend.position="none") +
  scale_y_continuous(limits=c(0,600)) 
save_plot("~/Dropbox (Timp Lab)/Timplab_writing/Manuscripts/180700_NatureMethods_RNAConsortia/figures/polyA/figure6d.pdf", p_ddx5, base_aspect_ratio = 1.5)


# Figure 6F
# spliced_df = read.delim("/dilithium/Data/Nanopore/rna/analysis/out_to_R/polya/splicedVCintron.txt", sep = "\t")
splicedAvg_df = read.delim("/dilithium/Data/Nanopore/rna/analysis/out_to_R/polya/splicedVCintron_avg.txt", sep = "\t")
p_spliced <- ggplot(splicedAvg_df, aes(x=type, y= polyA_length, fill = type)) +
  theme_cowplot(font_size = 14, font_family = "ArialMT", line_size = 1)+
  geom_violin(trim = FALSE,scale="width") + geom_boxplot(width = 0.2,outlier.shape = NA,fill="white") + 
  theme(strip.background =element_rect(fill="white"))+
  scale_x_discrete(labels = c(spliced= 'Spliced',intron_retained= 'Intron retained')) +
  scale_fill_manual(values = c("#00AFBB", "#E7B800")) +
  theme(legend.position="none") +
  scale_y_continuous(limits=c(0,600)) 
save_plot("~/Dropbox (Timp Lab)/Timplab_writing/Manuscripts/180700_NatureMethods_RNAConsortia/figures/polyA/figure6e.pdf", p_spliced, base_aspect_ratio = 1.5)
gd <- plot_grid(fig6a, p_nuc_mito,p_genes_1k_20k,p_ddx5,p_spliced, labels = c("a", "b", "c","d","e"), ncol = 2,label_fontfamily = "ArialMT",label_size = 20,align = "hv")

save_plot("~/Dropbox (Timp Lab)/Timplab_writing/Manuscripts/180700_NatureMethods_RNAConsortia/figures/polyA/181023_figure6_panel.pdf", gd,
          ncol = 2,
          nrow = 3, 
          base_aspect_ratio = 1.5
)



# orf_polya <- read.delim("/dilithium/Data/Nanopore/rna/analysis/out_to_R/polya/nvrna_polya_orf_lengths.txt", sep = "\t")
# 
# ggplot(orf_polya, aes(x=Median,y=orf_length)) +
#   geom_point() +
#   theme_cowplot(font_size = 14, font_family = "ArialMT", line_size = 1)+
#   theme(strip.background =element_rect(fill="white")) +
#   xlab("Median PolyA length") +
#   ylab("Isoform ORF length")
# 
# 
# orf_polya <- read.delim("/dilithium/Data/Nanopore/rna/analysis/out_to_R/polya/nvrna_polya_orf_lengths.txt", sep = "\t")
# 
# orf_polya <- orf_polya %>% 
#   mutate(ma = rollmean(orf_length, k = 100, fill = NA))
# 
# ggplot(orf_polya, aes(x=X,y=ma)) +
#   geom_line() +
#   theme_cowplot(font_size = 14, font_family = "ArialMT", line_size = 1)+
#   theme(strip.background =element_rect(fill="white")) +
#   xlab("Isoforms ranked by median poly(A) tail length") +
#   ylab("Isoform ORF length")
# 
# ggplot(orf_polya, aes(x=X,y=ma)) +
#   geom_line() +
#   theme_cowplot(font_size = 14, font_family = "ArialMT", line_size = 1)+
#   theme(strip.background =element_rect(fill="white")) +
#   xlab("Isoforms ranked by median poly(A) tail length") +
#   ylab("Isoform ORF length") + 
#   scale_x_continuous(limits = c(20000, 23000))


