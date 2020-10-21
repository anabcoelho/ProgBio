# importand pacotes
import sys
import pandas as pd
from Bio.Blast.Applications import *
from Bio import SeqIO

###### provisório
excel= "..\\data\\Tabela_1.xlsx"
desc= "..\\data\\Rdesconhecidus.fasta"
prolixus= "..\\dados\\Rprolixusptns.fasta"

# importando dados da linha de comando
#entrada tabela, multifasta desconhecido e multifasta conhecido
#l= sys.argv
#excel= l[1]
#desc= l[2]
#prolixus= l[3]



# Ler xlsx
with pd.ExcelFile(excel) as xlsx: #leitura arquivo
    df = pd.read_excel(xlsx)

# Importando fastas

#criando novas colunas

fatorNormalizacao_Rep1_CondA = 10**6/df['Rep1_CondA_Counts'].sum()
fatorNormalizacao_Rep2_CondA = 10**6/df['Rep1_CondA_Counts'].sum()
fatorNormalizacao_Rep1_CondB = 10**6/df['Rep1_CondB_Counts'].sum()
fatorNormalizacao_Rep2_CondB = 10**6/df['Rep2_CondB_Counts'].sum()

data_normalizado = {
    'gene' : df['gene'],
    'Rep1_CondA_CPM': df['Rep1_CondA_Counts']*fatorNormalizacao_Rep1_CondA,
    'Rep2_CondA_CPM': df['Rep2_CondA_Counts']*fatorNormalizacao_Rep2_CondA,
    'Rep1_CondB_CPM': df['Rep1_CondB_Counts']*fatorNormalizacao_Rep1_CondB,
    'Rep2_CondB_CPM': df['Rep2_CondB_Counts']*fatorNormalizacao_Rep2_CondB
}

df_normalizado = pd.DataFrame(data_normalizado, columns=['gene','Rep1_CondA_CPM','Rep2_CondA_CPM','Rep1_CondB_CPM','Rep2_CondB_CPM'])

print("Maior de valor expressão por réplica depois da normalização:")
print(df_normalizado.max(numeric_only=True).sort_values(ascending=False))