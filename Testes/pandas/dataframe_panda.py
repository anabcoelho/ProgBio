import pandas as pd

## criando dataframe

## um dataframe pode ser um dict de series
d = {'coluna1': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'coluna2': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd']),
     'coluna3': pd.Series([10., 2., 8.], index=['b', 'c', 'd'])}

## criando dataframe
df = pd.DataFrame(d)
print(df)

print("Imprimindo coluna 2:")
print(df['coluna2'])

## dataframes podem ter diferentes tipos de dados

data = {
    'Identificador': ['FBgn0034246', 'FBgn0250816', 'FBgn0283442'],
    'Símbolo': ['Dcr-2', 'AGO3', 'vas'],
    'Número de transcritos': [2, 4, 3]
}

print(data)

## criando dataframe
df = pd.DataFrame(data, columns=['Identificador','Símbolo','Número de transcritos'])
print(df)

## adicionando uma coluna
geneNome = ['Dicer-2','Argonaute 3','vasa']
df['Nome'] = geneNome
print(df)

### algumas informações sobre o dataframe:
print("Número de (linhas,colunas):")
print(df.shape)

print("Índice:")
print(df.index)

print("Quais são as colunas?")
print(df.columns)

print("Número de elementos não-nulos:")
print(df.count())

##################################################################################################
print("Total de transcritos = %d" % df['Número de transcritos'].sum())

##################################################################################################
print("Média de transcritos = %.2f" % df['Número de transcritos'].mean())

##################################################################################################
print("Mediana de transcritos = %.2f" % df['Número de transcritos'].median())

##################################################################################################
print("Maior número de transcritos = %d" % df['Número de transcritos'].max())



##################################################################################################
maxTranscrito = df['Número de transcritos'].max()
print("Gene com maior número de transcritos (linha inteira):")
print(df[df['Número de transcritos'] == maxTranscrito])
print("Gene com maior número de transcritos (nome):")
print(df[df['Número de transcritos'] == maxTranscrito]['Nome'])

##################################################################################################
print("Ordenando por símbolo:")
print(df.sort_values('Símbolo'))

##################################################################################################
print("Ordenando por quantidade de transcritos (crescente):")
print(df.sort_values('Número de transcritos'))

##################################################################################################
print("Ordenando por quantidade de transcritos (decrescente):")
print(df.sort_values('Número de transcritos', ascending=False))