### entrada das notas
entrada = []
while True:
    i=float(input("Digite a nota:"))
    if i == -1:
        break
    entrada.append(i)

def qtdvalores(x):
    #retorna a quantidade de valores
    return len(x)

def valoresinformados (x):
    #retorna os valores
    return x

def invertevalores (x):
    #inverte e imprime os valores invertidos
    x.reverse()
    for i in range(len(x)):
        print(x[i])

def somavalores (x):
    #calcula e retorna a soma
    soma=sum(x)
    return soma

def mediavalores(x):
    #calcula e retorna a média
    soma=somavalores(x) #chama a função soma
    media=soma/len(x)
    return media

def acimamedia (x):
    #calcula e retorna a quantidade de valores acima da média
    media=mediavalores(x)
    contagem=0
    for i in range(len(x)): #### função count tem como por?
        if x[i]> media:
            contagem+=1
    return contagem

print("Quantidade de valores:", qtdvalores(entrada))
print("Valores informados:", valoresinformados(entrada))
print("Valores invertidos:", invertevalores(entrada))
print("Soma dos valores:", somavalores(entrada))
print("Média dos valores:", mediavalores(entrada))
print("Quantidade de valores acima da média:", acimamedia(entrada))


