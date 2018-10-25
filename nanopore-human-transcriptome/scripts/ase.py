"""
Allele Specificity Analysis

By: Roham Razaghi (rrazagh1@jhu.edu), Timothy Gilpatrick (tgilpat@gmail.com)

Below are the bash commands to generate HapCUT2 and annotated vcf files:

$~/HapCUT2/build/extractHAIRS --nf 1 --ont 1 --bam NA12878-DirectRNA.pass.dedup.NoU.fastq.hg38.minimap2.sorted.bam --VCF Na128het.vcf --out NA12878het.fullgenome.extractHairs --ref /mithril/Data/NGS/Reference/human38/GRCH38.fa

$java -Xmx12g -jar ~/snpEff/snpEff/snpEff.jar -c ~/snpEff/snpEff/snpEff.config -d -v -canon -no-downstream -no-intergenic -no-upstream GRCh38.86 Na128het.vcf > Na128het.ann.canon.vcf

$ java -jar ~/snpEff/snpEff/SnpSift.jar extractFields -s "," -e "." Na128het.ann.canon.vcf CHROM POS REF ALT "ANN[].GENE" "ANN[].EFFECT" "GEN[*].GT" > Na128het.ann.canon.snpsift.vcf

"""

import numpy as np
import pandas as pd
import os
import subprocess
import pysam
from pybiomart import Dataset
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats

sns.set(color_codes=True)


# %matplotlib inline


def block_specificity(block_offset, block_alleles, variant_file):
    """
    This Function assigns specificity to each block.
    for more information about the extractHAIR command output:
    https://github.com/vibansal/HapCUT2/blob/master/old/FAQ.md
    """
    spec = ''
    genes = []
    num_variants = len(block_alleles)

    for i in range(num_variants):

        line = variant_file[int(block_offset) + i].split('\t')
        genotype = line[6].split('|')
        if block_alleles[i] == genotype[0]:
            spec += 'P'
        elif block_alleles[i] == genotype[1]:
            spec += 'M'
        chrom = line[0]
        genes.append(line[4].split(','))

    return chrom, genes, spec


def uniq(seq):
    """
    Output uniq values of a list
    """
    Set = set(seq)
    return list(Set)


def read_specificity(fragment_line, variant_file):
    """
    Finally assigning specificity to each read
    """
    genes_frag = []
    spec_frag = ''

    fragment = fragment_line.split(' ')
    num_blocks = int(fragment[0])
    for i in range(num_blocks):
        block_offset = fragment[5 + (2 * i)]
        block_alleles = fragment[6 + (2 * i)]
        chrom, genes, spec = block_specificity(block_offset, block_alleles, variant_file)
        genes_frag.append([y for x in genes for y in x])
        spec_frag += spec

    genes_frag = uniq([y for x in genes_frag for y in x])

    return chrom, genes_frag, spec_frag


def ase_threshold(row):
    if row['Maternal'] >= 0.8:
        val = 'Maternal'
    elif row['Paternal'] >= 0.8:
        val = 'Paternal'
    else:
        val = 'Unassigned'
    return val


def chr_type(f):
    autosome = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10',
                'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20',
                'chr21', 'chr22']
    if f['Chr'] in autosome:
        return 'Autosome'
    elif f['Chr'] == 'chrX':
        return 'Allosome'

def bam2py(bamfile):
    # this is probably not very efficient as it uses up a lot of memory but it'll do the job for now
    bamfile = pysam.AlignmentFile(bamfile, 'rb')
    name_indexed = pysam.IndexedReads(bamfile)
    name_indexed.build()
    header = bamfile.header.copy()
    return header,name_indexed



def ase2bam(reads, read_to_specificity,name_indexed, header, paternal_f='pat.bam',maternal_f='mat.bam', isoform=False, iso_f='isoform.bam'):
    def bam2igv(bam_f, nthreads=8):
        # https://www.programcreek.com/python/example/90607/pysam.sort
        out_b = bam_f.replace('.bam', '') + '_sorted.bam'
        pysam.sort("-@", str(nthreads), str(bam_f), "-o", str(out_b), catch_stdout=False)
        pysam.index(out_b, catch_stdout=False)
        os.remove(bam_f)

    if not isoform:
        paternal_reads = []
        maternal_reads = []
        for read in reads:
            if read_to_specificity[read] == 'M':
                maternal_reads.append(read)
            if read_to_specificity[read] == 'P':
                paternal_reads.append(read)

        out_p = pysam.Samfile(paternal_f, 'wb', header=header)
        out_m = pysam.Samfile(maternal_f, 'wb', header=header)
        for name in paternal_reads:
            iterator = name_indexed.find(name)
            for x in iterator:
                out_p.write(x)
        out_p.close()
        bam2igv(paternal_f)

        for name in maternal_reads:
            iterator = name_indexed.find(name)
            for x in iterator:
                out_m.write(x)
        out_m.close()
        bam2igv(maternal_f)

    elif isoform:

        out = pysam.Samfile(iso_f, 'wb', header=header)
        for name in reads:
            iterator = name_indexed.find(name)
            for x in iterator:
                out.write(x)
        out.close()
        bam2igv(iso_f)



if __name__ == '__main__':

    with open('/dilithium/Data/Nanopore/rna/analysis/hap/Na128het.ann.canon.snpsift.vcf') as g:

        variant_file = g.read().splitlines()

    fg = open('/dilithium/Data/Nanopore/rna/analysis/hap/NA12878het.fullgenome.extractHairs')
    outF = open("/dilithium/Data/Nanopore/rna/analysis/hap/NA12878_ase.txt", "w")
    for fragment_line in fg:

        chrom, genes, spec = read_specificity(fragment_line, variant_file)
        p_ratio = spec.count('P') / float(len(spec))
        m_ratio = spec.count('M') / float(len(spec))
        if p_ratio >= 0.75:
            allele_calling = 'P'
        elif m_ratio >= 0.75:
            allele_calling = 'M'
        else:
            allele_calling = '.'

        new_fragment_line = fragment_line[:-2] + ' ' + chrom + ' ' + ",".join([str(x) for x in genes]) + ' ' + str(
            p_ratio) + ' ' + str(m_ratio) + ' ' + allele_calling
        print(new_fragment_line, end="\n", file=outF)

    outF.close()
    fg.close()

    # --------------------------------------------------
    file = "/dilithium/Data/Nanopore/rna/analysis/hap/NA12878_ase.txt"
    f = open(file)
    read_to_specificity = {}
    read_to_chrom = {}

    for line in f:
        read_id = line.split(' ')[1]
        specificity = line.split(' ')[-1][0]
        chrom = line.split(' ')[-5]
        read_to_specificity[read_id] = specificity
        read_to_chrom[read_id] = chrom
    f.close()
    # --------------------------------------------------

    file = "/dilithium/Data/Nanopore/rna/isoforms/nvrna.180828.180927.read.isoform.map.nodup.txt"
    f = open(file)

    outF = open("/dilithium/Data/Nanopore/rna/analysis/out_to_R/nvrna_flair_ase.txt", "w")
    print("#Read_ID\tIsoform_ID\tAllele_specificity\tChr", end="\n", file=outF)

    genes_stats = {};
    isoforms_stats = {};
    gene_to_reads = {};
    isoform_to_reads = {};
    gene_to_chrom = {}
    for line in f:
        line_arr = line.strip().split('\t')
        read_id = line_arr[0]
        isoform_id = line_arr[1].split('_')[0].split('.')[0]
        try:

            gene_id = line_arr[1].split('_')[1].split('.')[0]
        except IndexError:
            continue
        if read_id in read_to_specificity.keys():
            gene_to_reads.setdefault(gene_id, []).append(read_id)
            isoform_to_reads.setdefault(isoform_id, []).append(read_id)
            new_line = line.strip() + '\t' + read_to_specificity[read_id] + '\t' + read_to_chrom[read_id]
            print(new_line, end="\n", file=outF)

            genes_stats.setdefault(gene_id, []).append(read_to_specificity[read_id])
            isoforms_stats.setdefault(isoform_id + '_' + gene_id, []).append(read_to_specificity[read_id])
            gene_to_chrom[gene_id] = read_to_chrom[read_id]

    outF2 = open("/dilithium/Data/Nanopore/rna/analysis/out_to_R/nvrna_gene_stats.txt", "w")
    print("Gene_ID\treads\tMaternal\tPaternal\tChr", end="\n", file=outF2)
    [print(str(k + '\t' + str(len(v)) + '\t' + str(float(v.count('M')) / len(v)) + '\t' + str(
        float(v.count('P')) / len(v)) + '\t' + gene_to_chrom[k]), end="\n", file=outF2) for k, v in genes_stats.items()]

    outF3 = open("/dilithium/Data/Nanopore/rna/analysis/out_to_R/nvrna_isoform_stats.txt", "w")
    print("isoform_ID\tGene_ID\treads\tMaternal\tPaternal", end="\n", file=outF3)
    [print(str(k.split('_')[0] + '\t' + k.split('_')[1] + '\t' + str(len(v)) + '\t' + str(
        float(v.count('M')) / len(v)) + '\t' + str(float(v.count('P')) / len(v))), end="\n", file=outF3) for k, v in
     isoforms_stats.items()]

    outF.close()
    outF2.close()
    outF3.close()
    f.close()
    # --------------------------------------------------
    df = pd.read_csv('/dilithium/Data/Nanopore/rna/analysis/out_to_R/nvrna_gene_stats.txt', sep='\t')
    df = df[(df.reads >= 5)]

    df['ASE'] = df.apply(ase_threshold, axis=1)

    dataset = Dataset(name='hsapiens_gene_ensembl', host='http://www.ensembl.org')

    conversion = dataset.query(attributes=['ensembl_gene_id', 'external_gene_name'])
    conversion.columns = ['Gene_ID', 'Gene_symbol']
    df_merge = pd.merge(df, conversion, how='inner', on=['Gene_ID'])

    df_merge['chr_type'] = df_merge.apply(chr_type, axis=1)
    df_merge.to_csv('/dilithium/Data/Nanopore/rna/analysis/out_to_R/nvrna_gene_stats.txt', header=True, index=False,
               sep='\t')

# --------------------------------------------------
    genes = list(gene_to_reads.keys())
    df = pd.read_csv('/dilithium/Data/Nanopore/rna/analysis/out_to_R/nvrna_isoform_stats.txt', sep='\t')
    df['ASE'] = df.apply(ase_threshold, axis=1)
    df = df[(df.reads >= 5)]
    df = pd.merge(df, conversion, how='inner', on=['Gene_ID'])
    df.to_csv('/dilithium/Data/Nanopore/rna/analysis/out_to_R/nvrna_isoform_stats.txt', header=True, index=False,
            sep='\t')
    isoform_ase = []
    for gene in genes:
        if len(df[(df.Gene_ID == gene) & (df.ASE == 'Paternal')]) >= 1 and len(
                df[(df.Gene_ID == gene) & (df.ASE == 'Maternal')]) >= 1:
            isoform_ase.append(gene)

    isoform_ase_df = df[(df.Gene_ID.isin(isoform_ase)) & (df.ASE != 'Unassigned')].sort_values(['reads', 'Gene_ID'],
                                                                                               ascending=False).reset_index(
        drop=True)

    isoform_ase_df.to_csv('/dilithium/Data/Nanopore/rna/analysis/out_to_R/nvrna_isoforms_ase.txt',
                          header=True, index=False, sep='\t')
# --------------------------------------------------

    header, name_indexed = bam2py('/dilithium/Data/Nanopore/rna/alignments/NA12878-DirectRNA.pass.dedup.NoU.fastq.hg38.minimap2.sorted.bam')

    # output maternal and paternal reads of gene ACTB
    ase2bam(gene_to_reads['ENSG00000075624'], read_to_specificity,name_indexed, header, paternal_f='/dilithium/Data/Nanopore/rna/analysis/igv/ACTB_paternal.bam',
              maternal_f='/dilithium/Data/Nanopore/rna/analysis/igv/ACTB_maternal.bam')

    # output 2 isoforms of IFIH1 gene
    ase2bam(isoform_to_reads['d7debd96-8a4a-46a7-8a9f-314847da89ac'], read_to_specificity, name_indexed, header, isoform=True,
            iso_f='/dilithium/Data/Nanopore/rna/analysis/igv/IFIH1_novel.bam')
    ase2bam(isoform_to_reads['ENST00000263642'], read_to_specificity, name_indexed, header,
            isoform=True,
            iso_f='/dilithium/Data/Nanopore/rna/analysis/igv/IFIH1_ENST00000263642.bam')

