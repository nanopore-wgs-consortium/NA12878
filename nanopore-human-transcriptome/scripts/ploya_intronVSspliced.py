"""
By: Roham Razaghi (rrazagh1@jhu.edu)

"""
import numpy as np
# Input files
isoform_file = open('/dilithium/Data/Nanopore/rna/isoforms/nvrna.180828.180927.read.isoform.map.nodup.txt')
polya_file = open('/dilithium/Data/Nanopore/rna/polyA/NA12878_DirectRNA_polya_primary.txt')
psl_file = open('/dilithium/Data/Nanopore/rna/isoforms/nvrna.180828.180927.isoforms.renamed.psl')
# Output files
splicedVSintron_file = '/dilithium/Data/Nanopore/rna/analysis/out_to_R/polya/splicedVCintron_avg.txt'


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


for line in polya_file:
    line_arr = line.strip().split('\t')
    read_id = line_arr[0]
    chrom = line_arr[1]
    polya_length = line_arr[8]
    qc_taq = line_arr[9]
    if qc_taq == 'PASS' and read_id in read_to_isogene.keys() and float(polya_length) < 600:

        isoform_to_polya_length.setdefault(read_to_isogene[read_id], []).append(float(polya_length))
        iso_to_polya.setdefault(read_to_iso[read_id], []).append(float(polya_length))
        gene_to_polya_length.setdefault(read_to_gene[read_id], []).append(float(polya_length))
        polya_lengths.append(float(polya_length))
polya_file.close()


lines = psl_file.readlines()
psl_file.close()

intron_retained = []
spliced = []
intron_retained_unproductive = []
intron_retained_productive = []
intron_retained_lnc = []
spliced_unproductive = []
spliced_productive = []
spliced_lnc = []
for line in lines:
    line_arr = line.strip().split('\t')
    isoform_name = line_arr[9].split('_')[0].split('.')[0]
    read_count = line_arr[23]
    if int(read_count) >= 20:

        if int(line_arr[21]) == 0:
            spliced.append(isoform_name)
            if int(line_arr[22]) == 0:
                spliced_productive.append(isoform_name)
            if int(line_arr[22]) == 1:
                spliced_unproductive.append(isoform_name)
            if int(line_arr[22]) == 2:
                spliced_lnc.append(isoform_name)

        if int(line_arr[21]) == 1:
            intron_retained.append(isoform_name)
            if int(line_arr[22]) == 0:
                intron_retained_productive.append(isoform_name)
            if int(line_arr[22]) == 1:
                intron_retained_unproductive.append(isoform_name)
            if int(line_arr[22]) == 2:
                intron_retained_lnc.append(isoform_name)

intron_retained_polya = []
spliced_polya = []
intron_retained_unproductive_polya = []
intron_retained_productive_polya = []
intron_retained_lnc_polya = []
spliced_unproductive_polya = []
spliced_productive_polya = []
spliced_lnc_polya = []
# for k, v in iso_to_polya.items():
#     if k in intron_retained:
#         intron_retained_polya.extend(v)
#     if k in intron_retained_lnc:
#         intron_retained_lnc_polya.extend(v)
#     if k in intron_retained_productive:
#         intron_retained_productive_polya.extend(v)
#     if k in intron_retained_unproductive:
#         intron_retained_unproductive_polya.extend(v)
#
#     if k in spliced:
#         spliced_polya.extend(v)
#     if k in spliced_lnc:
#         spliced_lnc_polya.extend(v)
#     if k in spliced_productive:
#         spliced_productive_polya.extend(v)
#     if k in spliced_unproductive:
#         spliced_unproductive_polya.extend(v)
for k, v in iso_to_polya.items():
    if k in intron_retained:
        intron_retained_polya.append(np.mean(v))
    if k in intron_retained_lnc:
        intron_retained_lnc_polya.append(np.mean(v))
    if k in intron_retained_productive:
        intron_retained_productive_polya.append(np.mean(v))
    if k in intron_retained_unproductive:
        intron_retained_unproductive_polya.append(np.mean(v))

    if k in spliced:
        spliced_polya.append(np.mean(v))
    if k in spliced_lnc:
        spliced_lnc_polya.append(np.mean(v))
    if k in spliced_productive:
        spliced_productive_polya.append(np.mean(v))
    if k in spliced_unproductive:
        spliced_unproductive_polya.append(np.mean(v))
# outF = open(splicedVSintron_file, "w")
# print("polyA_length\ttype\tsubtype", end="\n", file=outF)
# for k, v in iso_to_polya.items():
#     # if k in intron_retained:
#     #     intron_retained_polya.extend(v)
#     if k in intron_retained_lnc:
#         print(v+'\t' + 'intron_retained' + '\t' + 'intron_retained_lnc', end="\n", file=outF)
#         # intron_retained_lnc_polya.extend(v)
#     if k in intron_retained_productive:
#         print(v + '\t' + 'intron_retained' + '\t' + 'intron_retained_productive', end="\n", file=outF)
#         # intron_retained_productive_polya.extend(v)
#     if k in intron_retained_unproductive:
#         print(v + '\t' + 'intron_retained' + '\t' + 'intron_retained_unproductive', end="\n", file=outF)
#         # intron_retained_unproductive_polya.extend(v)
#
#     # if k in spliced:
#     #     print(v + '\t' + 'spliced' + '\t' + 'spliced_lnc', end="\n", file=outF)
#     #     spliced_polya.extend(v)
#     if k in spliced_lnc:
#         print(v + '\t' + 'spliced' + '\t' + 'spliced_lnc', end="\n", file=outF)
#         # spliced_lnc_polya.extend(v)
#     if k in spliced_productive:
#         print(v + '\t' + 'spliced' + '\t' + 'spliced_productive', end="\n", file=outF)
#         # spliced_productive_polya.extend(v)
#     if k in spliced_unproductive:
#         print(v + '\t' + 'spliced' + '\t' + 'spliced_unproductive', end="\n", file=outF)
#         # spliced_unproductive_polya.extend(v)
#
outF = open(splicedVSintron_file, "w")
print("polyA_length\ttype\tsubtype", end="\n", file=outF)
[print(str(str(v) + '\t' + 'spliced' + '\t' + 'spliced_lnc'), end="\n", file=outF) for v in spliced_lnc_polya]
[print(str(str(v) + '\t' + 'spliced' + '\t' + 'spliced_productive'), end="\n", file=outF) for v in spliced_productive_polya]
[print(str(str(v) + '\t' + 'spliced' + '\t' + 'spliced_unproductive'), end="\n", file=outF) for v in spliced_unproductive_polya]
[print(str(str(v) + '\t' + 'intron_retained' + '\t' + 'intron_retained_lnc'), end="\n", file=outF) for v in intron_retained_lnc_polya]
[print(str(str(v) + '\t' + 'intron_retained' + '\t' + 'intron_retained_productive'), end="\n", file=outF) for v in intron_retained_productive_polya]
[print(str(str(v) + '\t' + 'intron_retained' + '\t' + 'intron_retained_unproductive'), end="\n", file=outF) for v in intron_retained_unproductive_polya]

outF.close()
