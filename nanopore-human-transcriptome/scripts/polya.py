"""
By: Roham Razaghi (rrazagh1@jhu.edu)

"""
import numpy as np
from pybiomart import Dataset
import pandas as pd

# Input files
isoform_file = open('/dilithium/Data/Nanopore/rna/isoforms/nvrna.180828.180927.read.isoform.map.nodup.txt')
polya_file = open('/dilithium/Data/Nanopore/rna/polyA/NA12878_DirectRNA_polya_primary.txt')
# Output files
polya_dataframe = '/dilithium/Data/Nanopore/rna/analysis/out_to_R/polya/nvrna_polya_dataframe.txt'
polya_gene_stat = '/dilithium/Data/Nanopore/rna/analysis/out_to_R/polya/nvrna_polya_genes_stat.txt'
polya_isoform_stat = '/dilithium/Data/Nanopore/rna/analysis/out_to_R/polya/nvrna_polya_isoforms_stat.txt'


read_to_gene = {};read_to_isogene = {};isoform_to_polya_length = {};gene_to_polya_length = {};polya_lengths = [];read_to_iso = {};iso_to_polya = {}
for line in isoform_file:
    line_arr = line.strip().split('\t')
    read_id = line_arr[0]
    isoform_id = line_arr[1].split('_')[0].split('.')[0]
    gene_id = line_arr[1].split('_')[1].split('.')[0]
    iso_gene_id = isoform_id + '_' + gene_id
    read_to_isogene[read_id] = iso_gene_id
    read_to_gene[read_id] = gene_id
    read_to_iso[read_id] = isoform_id
isoform_file.close()


outF = open(polya_dataframe, "w")
print("Isoform_ID\tGene_ID\tChrom\tPolyA_length", end="\n", file=outF)
for line in polya_file:
    line_arr = line.strip().split('\t')
    read_id = line_arr[0]
    chrom = line_arr[1]
    polya_length = line_arr[8]
    qc_taq = line_arr[9]
    if qc_taq == 'PASS' and read_id in read_to_isogene.keys():
        print(read_to_isogene[read_id].split('_')[0] + '\t' + read_to_isogene[read_id].split('_')[1] +
              '\t' + chrom + '\t' + polya_length, end="\n", file=outF)

        isoform_to_polya_length.setdefault(read_to_isogene[read_id], []).append(float(polya_length))
        iso_to_polya.setdefault(read_to_iso[read_id], []).append(float(polya_length))
        gene_to_polya_length.setdefault(read_to_gene[read_id], []).append(float(polya_length))
        polya_lengths.append(float(polya_length))
polya_file.close()
outF.close()


outF1 = open(polya_gene_stat, "w")
print("Gene_ID\tReads\tMean\tMedian\tSD", end="\n", file=outF1)
[print(str(k + '\t' + str(len(v)) + '\t' + str(np.mean(v)) + '\t' + str(np.median(v)) + '\t' + str(np.std(v))),
       end="\n", file=outF1) for k, v in gene_to_polya_length.items()]
outF1.close()


outF2 = open(polya_isoform_stat, "w")
print("Isoform_ID\tGene_ID\tReads\tMean\tMedian\tSD", end="\n", file=outF2)
[print(str(k.split('_')[0] + '\t' + k.split('_')[1] + '\t' + str(len(v)) + '\t' + str(np.mean(v)) + '\t' + str(
    np.median(v)) + '\t' + str(np.std(v))), end="\n", file=outF2) for k, v in isoform_to_polya_length.items()]
outF2.close()



dataset = Dataset(name='hsapiens_gene_ensembl', host='http://www.ensembl.org')
conversion = dataset.query(attributes=['ensembl_gene_id', 'external_gene_name'])
conversion.columns = ['Gene_ID', 'Gene_symbol']

for file in [polya_isoform_stat,polya_gene_stat,polya_dataframe]:
    df = pd.read_csv(file, sep='\t')
    df_merge = pd.merge(df, conversion, how='inner', on=['Gene_ID'])
    df_merge.to_csv(file, header=True, index=False, sep='\t')
