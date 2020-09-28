import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt


#### ATENÇÃO: Instale o pacote xlrd >= 1.0.0 para ler arquivos Excel
# ## Use pip
# ou
## conda install -c anaconda xlrd
#
## ou diretamente pelo PyCharm
## se dada der certo, use o arquivo em formato CSV

## lendo arquivo excel
with pd.ExcelFile('../data/quantificacao_exemplo.xlsx') as xlsx:
    df = pd.read_excel(xlsx, 'Counts')

## visualizando as primeiras linhas com head()
#print(df.head())

## visualizando tudo
#print(df)


#print("Quais são as colunas?")
#print(df.columns)

#print("Qual o tamanho deste arquivo:")
#print(df.shape)

##################################################################################################
#print("Média de expressão não-normalizada da réplica Rep1_CondA = %.2f" % df['Rep1_CondA_Counts'].mean())
##################################################################################################
#print("Média de expressão não-normalizada da réplica Rep2_CondA = %.2f" % df['Rep2_CondA_Counts'].mean())
##################################################################################################
#print("Média de expressão não-normalizada da réplica Rep1_CondB = %.2f" % df['Rep1_CondB_Counts'].mean())
##################################################################################################
#print("Média de expressão não-normalizada da réplica Rep2_CondB = %.2f" % df['Rep2_CondB_Counts'].mean())
##################################################################################################

#print("Média de expressão em um único comando =")
#print(df.mean(numeric_only=True))

#print("Mediana de expressão em um único comando =")
#print(df.median(numeric_only=True))

#print("Máximo de expressão não-normalizada em um único comando:")
#print(df.max(numeric_only=True))

#print("Mínimo de expressão não-normalizada em um único comando:")
#print(df.min(numeric_only=True))

######################################
### normalizando os niveis de expressão por
### CPM = numero de counts * 10**6/total numero de counts

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

print("Maior de valor expressão por réplica antes da normalização:")
print(df.max(numeric_only=True).sort_values(ascending=False))

print("Maior de valor expressão por réplica depois da normalização:")
print(df_normalizado.max(numeric_only=True).sort_values(ascending=False))

### juntando dataframes

print("Verificando as primeiras linhas de df:")
print(df.head())

print("Verificando as primeiras linhas de df_normalizado:")
print(df_normalizado.head())

print("Juntando df e df_normalizado baseado nas chaves mais a esquerda (ou seja, gene):")
df_final = pd.merge(df,df_normalizado)
print(df_final.head())

print("Genes com expressão normalizada maior que 100:")
print(df_normalizado[df_normalizado['Rep1_CondA_CPM'] > 100]['gene'])

print("Salvando o arquivo Excel:")
df_final.to_excel("../data/quantificao_normalizada.xlsx",sheet_name="CPM")

### Criando um histograma dos valores de CPM para replica 1 na condicao A
plot1 = df_normalizado["Rep1_CondA_CPM"].plot.hist(bottom=0.1)

## Configurando o plot
plot1.set_yscale("log")
plot1.set_xlabel("CPM")
plot1.set_ylabel("Número de genes")
plot1.set_title("Réplica 1 Condição A - CPM")

## salvando a figura como pdf
figure1 = plot1.get_figure()
figure1.savefig("../data/rep1_condA_cpm.pdf")
##########################################################################


## usando matplotlib
### subplot cria uma figura (fig) com um plot (plot2)
fig,plot2 = plt.subplots()
plot2.hist([df_normalizado['Rep1_CondA_CPM'],df_normalizado['Rep2_CondA_CPM']], bottom=0.1, label=['Réplica 1','Réplica 2'])
plot2.set_xlabel("CPM")
plot2.set_yscale("log")
plot2.set_ylabel("Número de genes")
plot2.set_title("Condição A - CPM")
plot2.legend(loc='upper right')
figure2 = plot2.get_figure()
figure2.savefig("../data/rep1_vs_rep2_condA_cpm.pdf")

print("Genes com CPM > 7000")
print(df_normalizado[(df_normalizado['Rep1_CondA_CPM'] > 7000) | (df_normalizado['Rep2_CondA_CPM'] > 7000)])