# importando pacotes

import sys
import pandas as pd
from Bio.Blast.Applications import *
from Bio import SeqIO

###### locais dos arquivos e nomes #########
#excel= "..\\data\\Tabela_1.xlsx"
#desc= "..\\data\\Rdesconhecidus.fasta"
#prolixus= "..\\data\\Rprolixusptns.fasta"

#importando dados da linha de comando
#entrada tabela, multifasta desconhecido e multifasta conhecido
entrada= sys.argv
excel= entrada[1]
desc= entrada[2]
prolixus= entrada[3]

# Ler xlsx
with pd.ExcelFile(excel) as xlsx: #leitura arquivo
    df = pd.read_excel(xlsx)

#criando novas colunas para df para normalização
fnorm_Rep1_A = 10**6/df['Rep1_A'].sum()
fnorm_Rep2_A = 10**6/df['Rep2_A'].sum()
fnorm_Rep1_B = 10**6/df['Rep1_B'].sum()
fnorm_Rep2_B= 10**6/df['Rep2_B'].sum()

data_normalizado = {
    'gene_id' : df['gene_id'],
    'Rep1_A': df['Rep1_A'],
    'Rep2_A': df['Rep2_A'],
    'Rep1_B': df['Rep1_B'],
    'Rep2_B': df['Rep2_B'],

    'Rep1_A_CPM': df['Rep1_A']*fnorm_Rep1_A,
    'Rep2_A_CPM': df['Rep2_A']*fnorm_Rep2_A,
    'Rep1_B_CPM': df['Rep1_B']*fnorm_Rep1_B,
    'Rep2_B_CPM': df['Rep2_B']*fnorm_Rep2_B
}

df_norm = pd.DataFrame(data_normalizado)
#novo dataframe

#CPM média
Cond_A_CPM_media=(df_norm['Rep1_A_CPM'] + df_norm['Rep2_A_CPM'])/2
Cond_B_CPM_media=(df_norm['Rep1_B_CPM'] + df_norm['Rep2_B_CPM'])/2

data_final = {
    'gene_id' : df['gene_id'],
    'Rep1_A': df['Rep1_A'],
    'Rep2_A': df['Rep2_A'],
    'Rep1_B': df['Rep1_B'],
    'Rep2_B': df['Rep2_B'],

    'Rep1_A_CPM': df['Rep1_A']*fnorm_Rep1_A,
    'Rep2_A_CPM': df['Rep2_A']*fnorm_Rep2_A,
    'Rep1_B_CPM': df['Rep1_B']*fnorm_Rep1_B,
    'Rep2_B_CPM': df['Rep2_B']*fnorm_Rep2_B,

    'Cond_A_CPM_media': Cond_A_CPM_media,
    'Cond_B_CPM_media': Cond_B_CPM_media
}

df_final = pd.DataFrame(data_final)

## ordenando por condição
df_final= df_final.sort_values('Cond_A_CPM_media', ascending=False)
seleçãoA= df_final.head() ### head, sem nenhum argumento, escolhe as 5 primeiras linhas
df_final= df_final.sort_values('Cond_B_CPM_media', ascending=False)
seleçãoB= df_final.head()

#ordenando os genes
seleção= seleçãoA.append(seleçãoB)
seleção.sort_index(inplace=True)
seleção.drop_duplicates(inplace=True) #retirando duplicatas
#lista com os genes em ordem de ID
genes=list(seleção["gene_id"])

#      escrever os fastas dos 10 melhores genes
arquivodesconhecidus = open(desc,'r')

#Dividindo multifasta para fastas
x=1
y=0
for i in SeqIO.parse(arquivodesconhecidus, "fasta"): #loop
    if i.id == genes[y]:
        fname = "..\\data\\gene_%d.fasta" % (x)
        with open(fname, "w") as handle: #escrita
            count = SeqIO.write(i,handle, "fasta")
        y+=1
        if y == len(genes):
            break
    x+=1


    #blastx
def blastx (seq, seqalvo, outputlocal):
    ### função que recebe os locais das sequencias e o output e roda o blastx, retorna o melhor hit em uma lista.
    blastx_path = "C:\\Program Files\\NCBI\\blast-2.10.1+\\bin\\blastx"
    ## NcbiblastxCommandline - nucleotideo -> traduz para proteina vs proteina
    linha_de_comando_blastx = NcbiblastxCommandline(cmd=blastx_path,
                                                query=seq,
                                                subject=seqalvo,
                                                outfmt=6,
                                                out=outputlocal,
                                                evalue=0.05)

    #

    stdout, stderr = linha_de_comando_blastx()

        # Abrindo resultado
    blast_result = open(meuOutput, "r")
##### indíces para os resultados do blast em formato 6 ("outfmt=6")

    qseqid = 0 #query  sequence id
    sseqid = 1 # subject  ptn id
    pident = 2 # percentage of identical matches
    length = 3 # alignment length (sequence overlap)
    mismatch = 4 # number of mismatches
    gapopen = 5 # number of gap openings
    qstart = 6 # start of alignment in query
    qend = 7 # end of alignment in query
    sstart = 8 # start of alignment in subject
    send = 9 # end of alignment in subject
    evalue = 10 # expect value
    bitscore = 11 # bit score

    results = blast_result.read()
    s = results.split('\n')
    bitanterior=1.0
    for linha in s:
        hit = linha.split('\t')
        if len(hit) != 12:
             break
        bit = hit[bitscore]
        bit=float (bit)
        if bitanterior < bit:
            maxi=hit
            bitanterior = bit

    return [maxi[qseqid], maxi[sseqid], maxi[bitscore], maxi[evalue]]
    #só precisarei desses valores, porém pode-se retornar toda a lista maxi

## Rodando blastx para todos os genes
## lista genes tem o nome dos arquivos
blastlist=[] ## para saída do blastx
for i in genes:
    sequencia = "..\\data\\%s.fasta" %i

    meuOutput = "..\\data\\outputblastx_%s.txt" %i
    blastlist.append(blastx(sequencia, prolixus, meuOutput))

blastDF=pd.DataFrame(blastlist, columns= ["gene_id", "ptn_id", "bitscore","e-value"])

#ordenando para menor e-value e maior bitscore
blastDF=blastDF.sort_values('e-value', ignore_index=True)
blastDF= blastDF.sort_values('bitscore',  ascending=False, ignore_index=True)

#### RESULTADOS
HIT=blastDF.head(1)
HIT=HIT.values.tolist()
HIT=HIT[0]

### pegando os valores do gene no df anterior (seleção)
Gene_Correto= seleção[seleção['gene_id'] == HIT[0]]
Gene_Correto=Gene_Correto.values.tolist()
Gene_Correto=Gene_Correto[0] # Cond_A_CPM_media  Cond_B_CPM_media são os dois últimos

#### hora dos prints
print("Gene encontrado:", HIT[0])
print("CPM média da condição A:", Gene_Correto[-2])
print("CPM média da condição B:", Gene_Correto[-1])
print("Id da proteína encontrada:", HIT[1])


