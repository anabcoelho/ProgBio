import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## criando series
densidades = pd.Series([0.53, 0.97, 0.86, 1.53, 1.9])

## criando um array de indices
indexElementos = ["Li","Na","K","Rb","Cs"]

## adicionando indice
densidades.index = indexElementos

print("Imprimindo densidades adicionando indices depois:")
print(densidades)

## definindo indices ao criar series
densidades = pd.Series([0.53, 0.97, 0.86, 1.53, 1.9],index=["Li","Na","K","Rb","Cs"])
print("Imprimindo densidades com indices ao criar o series:")
print(densidades)

## atualizando os indices
novoIndex = ["a", "b", "c", "d", "e"]
densidades.index = novoIndex

print("Alterando os indices:")
print(densidades)

## criando series a partir de dict
meuDict = {"Li":0.53,"Na":0.97,"K":0.86,"Rb":1.53,"Cs":1.9}
densidades = pd.Series(meuDict)

print("Criando series a partir de um dict:")
print(densidades)

print("Imprimindo a partir do segundo elemento:")
print(densidades[1:])

print("Imprimindo o quarto elemento:")
print(densidades[3:4])

print("Imprimindo a densidade do quarto elemento a partir do indice:")
print(densidades["Rb"])

print("Imprimindo os elementos do primeiro ao ultimo indice (nao incluido)")
print(densidades[:-1])

## obter elementos maiores que a media das densidades
### calcula media

media = np.mean(densidades)
print("A média das densidades é %f" % media)

print("Os elementos com densidade maior que a média:")

## usa operador para selecionar os elementos de densidades maior que a media
print(densidades[densidades > media])

print("Densidades original:")
print(densidades)

print("Densidades removendo elementos usando drop:")

densidades = densidades.drop(["Rb", "Cs"])
print(densidades)