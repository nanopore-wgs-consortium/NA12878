"""
By: Roham Razaghi (rrazagh1@jhu.edu)

"""
import numpy as np
from pybiomart import Dataset
import pandas as pd

# input files
isoform_file = open('/dilithium/Data/Nanopore/rna/isoforms/nvrna.180828.180927.read.isoform.map.nodup.txt')
evalign_file = open('/dilithium/Data/Nanopore/rna/evalign/180716_dRNAall.mq5_GGACU.evalign.txt')

# output files
evalign_df = "/dilithium/Data/Nanopore/rna/analysis/out_to_R/mod/nvrna_evalign_GGACU_dataframe.txt"
evalign_stat =  "/dilithium/Data/Nanopore/rna/analysis/out_to_R/mod/nvrna_evalign_GGACU_stats.txt"


read_to_isogene = {}
data_dict = {}


for line in isoform_file:
    line_arr = line.strip().split('\t')
    read_id = line_arr[0]
    isoform_id = line_arr[1].split('_')[0].split('.')[0]
    gene_id = line_arr[1].split('_')[1].split('.')[0]
    iso_gene_id = gene_id + '_' + isoform_id
    read_to_isogene[read_id] = iso_gene_id


outF2 = open(evalign_df, "w")
print("Position\tIsoform\tGene_ID\tEvent_mean", end="\n", file=outF2)
for line in evalign_file:
    read_id = line.split('\t')[3]
    event_mean = line.split('\t')[6]
    model_kmer = line.split('\t')[9]
    pos = line.split('\t')[1]

    if read_id in read_to_isogene.keys() and model_kmer == 'GGACU':
        key = read_to_isogene[read_id] + '_' + pos
        print(pos + '\t' + key.split('_')[1] + '\t' + key.split('_')[0] + '\t' + event_mean, end="\n", file=outF2)
        data_dict.setdefault(key, []).append(float(event_mean))


outF = open(evalign_stat, "w")
print("Position\tIsoform\tGene_ID\tReads\tEvent_mean\tEvent_median\tSD\tDistance", end="\n", file=outF)
[print(k.split('_')[2] + '\t' + k.split('_')[1] + '\t' + k.split('_')[0] + '\t' + str(len(v)) + '\t' + str(
    np.mean(v)) + '\t' + str(np.median(v)) + '\t' + str(np.std(v)) + '\t' + str(np.mean(v) - 123.83), end="\n",
       file=outF) for k, v in data_dict.items()]

evalign_file.close()
isoform_file.close()
outF.close()
outF2.close()


dataset = Dataset(name='hsapiens_gene_ensembl', host='http://www.ensembl.org')

conversion = dataset.query(attributes=['ensembl_gene_id', 'external_gene_name'])
conversion.columns = ['Gene_ID', 'Gene_symbol']

for file in [evalign_stat,evalign_df]:
    df = pd.read_csv(file, sep='\t')
    df_merge = pd.merge(df, conversion, how='inner', on=['Gene_ID'])
    df_merge.to_csv(file, header=True, index=False, sep='\t')
