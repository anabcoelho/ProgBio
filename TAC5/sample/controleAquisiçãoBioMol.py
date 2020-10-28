#importando
import operacoesCompra as OC

dicionario={}#dicionário vazio p/ importação
while True:
    Produto= input("Digite o produto:")
    if Produto == "-1":### a entrada é uma str
        break
    Preço= float(input("Digite o preço:"))
    if Preço == -1:
        break
    Quantidade=int(input("Digite a quantidade:"))
    if Quantidade == -1:
        break
    dicionario[Produto]=[Preço,Quantidade]

#chamada das funções importadas
OC.imprimeprodutos(dicionario)
print('-------')
OC.imprimequantidades(dicionario)
print("-------")
OC.calculaTotalCompra(dicionario)