

def imprimeprodutos (dictionary):
    #imprime nome dos produtos a serem comprados
    print("Produtos:", list(dictionary.keys()))



def imprimequantidades (dictionary):
    ### quantidades de cada produto a ser comprado
    keys= list(dictionary.keys())
    values= list(dictionary.values())
    for i in range(len(dictionary)):

        print("produto:", keys[i], "quantidade:", values[i][1])

def calculaTotalCompra (dictionary):
    ## retorna o valor total das compras
    values = list(dictionary.values())
    soma=0
    for i in range(len(dictionary)):
        soma+=(values[i][0]*values[i][1])
    print('Soma dos preços:', soma)

