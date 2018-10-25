library(tidyverse)
library(cowplot)
require(magick)
library(extrafont)

# Figure 7A
df = read.delim("/dilithium/Data/Nanopore/rna/analysis/out_to_R/mod/EEF2_events.txt", sep = "\t")
df_nvrna <- df %>% filter(dataset == "nvRNA")
df_oligo <- df %>% filter(dataset == "oligo")

mod_df = read.delim("/dilithium/Data/Nanopore/rna/analysis/out_to_R/mod/nvrna_evalign_GGACU_dataframe.txt",sep = "\t")
actb <- mod_df %>% filter(Position == "5527740", Isoform == "6dc7f0e7-51c7-462d-afd9-b133adcb173d" | Isoform == "ENST00000493945")
p_eef2_nvrna <- ggplot(df_nvrna, aes(x = event_mean, fill= state)) +
  theme_cowplot(font_size = 14, font_family = "ArialMT", line_size = 1)+
  geom_density(alpha= 0.5) +
  # facet_wrap(~ dataset,ncol=2) +
  theme(strip.background =element_rect(fill="white")) +
  scale_fill_manual(name="",values = c(Modified="#1f77b4", Unmodified="#ff7f0e"),labels=c("GGm6ACU", "GGACU")) +
  geom_segment(aes(x = 123.8, xend = 123.8, y = 0, yend = 0.15,linetype= "Pore Model"),color="black",size=1 ) +
  scale_linetype_manual(name="",values = c("Pore Model"=2)) +
  theme(legend.position="top")
save_plot("~/Dropbox (Timp Lab)/Timplab_writing/Manuscripts/180700_NatureMethods_RNAConsortia/figures/mod/figure7a.pdf", p_eef2_nvrna, base_aspect_ratio = 1.5)
# Figure 7B

# Figure 7C
p_eef2_oligo <- ggplot(df_oligo, aes(x = event_mean, fill= state)) +
  theme_cowplot(font_size = 14, font_family = "ArialMT", line_size = 1)+
  geom_density(alpha= 0.5) +
  # facet_wrap(~ dataset,ncol=2) +
  theme(strip.background =element_rect(fill="white")) +
  scale_fill_manual(name="",values = c(Modified="#1f77b4", Unmodified="#ff7f0e"),labels=c("GGm6ACU", "GGACU")) +
  geom_segment(aes(x = 123.8, xend = 123.8, y = 0, yend = 0.15,linetype= "Pore Model"),color="black",size=1 ) +
  scale_linetype_manual(name="",values = c("Pore Model"=2)) +
  theme(legend.position="top")
save_plot("~/Dropbox (Timp Lab)/Timplab_writing/Manuscripts/180700_NatureMethods_RNAConsortia/figures/mod/figure7c.pdf", p_eef2_oligo, base_aspect_ratio = 1.5)

# Figure 7D
p_actb <- ggplot(actb, aes(x = Event_mean, fill= Isoform)) +
  theme_cowplot(font_size = 14, font_family = "ArialMT", line_size = 1)+
  geom_density(alpha= 0.7) +
  theme(strip.background =element_rect(fill="white")) +
  scale_fill_manual(name="",values = c("#7BB274", "#FEB308"),labels=c("ACTB Isoform 6dc", "ACTB Isoform 945")) +
  geom_segment(aes(x = 123.8, xend = 123.8, y = 0, yend = 0.09,linetype= "Pore Model"),color="black",size=1 ) +
  scale_linetype_manual(name="",values = c("Pore Model"=2)) +
  theme(legend.position="top")
save_plot("~/Dropbox (Timp Lab)/Timplab_writing/Manuscripts/180700_NatureMethods_RNAConsortia/figures/mod/figure7d.pdf", p_actb, base_aspect_ratio = 1.5)

# Panel Figure
# bottom_row <- plot_grid(p_eef2, p_actb, labels = c('b','c'), align = 'h',rel_widths = c(1,1))

gd <- plot_grid(p_eef2_nvrna,NULL,p_eef2_oligo,p_actb, labels = c("a", "b","c","d"), ncol = 2,label_fontfamily = "ArialMT",label_size = 20,align = "hv")

save_plot("~/Dropbox (Timp Lab)/Timplab_writing/Manuscripts/180700_NatureMethods_RNAConsortia/figures/mod/102218_figure7.pdf", gd,
          ncol = 2,
          nrow = 3, 
          base_aspect_ratio = 1.5
)

