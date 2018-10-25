"""
By: Roham Razaghi (rrazagh1@jhu.edu)

"""
evalign_file_drna = open('/dilithium/Data/Nanopore/rna/evalign/eef2/dRNA.EEF2.GGACU.evalign.txt')
evalign_file_ivt = open('/dilithium/Data/Nanopore/rna/evalign/eef2/IVT.EEF2.GGACU.evalign.txt')
evalign_file_oligo = open('/dilithium/Data/Nanopore/rna/evalign/eef2/180612_evalign.m6aoligo.sub.txt')

data_dict = {}
outF = open("/dilithium/Data/Nanopore/rna/analysis/out_to_R/mod/EEF2_events.txt", "w")
print("state\tevent_mean\tdataset", end="\n", file=outF)

for line in evalign_file_drna:
    read_id = line.split('\t')[3]
    event_mean = line.split('\t')[6]
    model_kmer = line.split('\t')[9]
    pos = line.split('\t')[1]

    if pos == '3976325' and model_kmer == 'GGACU':
        print('Modified' + '\t' + event_mean + '\t' + 'nvRNA', end="\n", file=outF)
for line in evalign_file_ivt:
    read_id = line.split('\t')[3]
    event_mean = line.split('\t')[6]
    model_kmer = line.split('\t')[9]
    pos = line.split('\t')[1]

    if pos == '3976325' and model_kmer == 'GGACU':
        print('Unmodified' + '\t' + event_mean + '\t' + 'nvRNA', end="\n", file=outF)
for line in evalign_file_oligo:
    read_id = line.split('\t')[3]
    event_mean = line.split('\t')[6]
    model_kmer = line.split('\t')[9]
    pos = line.split('\t')[1]

    if pos == '1754' and model_kmer == 'GGACT':
        print('Modified' + '\t' + event_mean + '\t' + 'oligo', end="\n", file=outF)

    if pos == '1773' and model_kmer == 'GGACT':
        print('Unmodified' + '\t' + event_mean + '\t' + 'oligo', end="\n", file=outF)

evalign_file_drna.close()
evalign_file_ivt.close()
evalign_file_oligo.close()
outF.close()

