#
dicionário={}
while True:
    Produto= input("Digite o produto:")
    if Produto == -1:
        break
    Preço= float(input("Digite o preço:"))
    if Preço == -1:
        break
    Quantidade=int(input("Digite a quantidade:"))
    if Quantidade == -1:
        break
    dicionário[Produto]=[Preço,Quantidade]

print(dicionário)