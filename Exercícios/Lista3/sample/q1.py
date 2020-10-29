#input na lista
entrada = [float(i) for i in input("Digite números:").split()]
# soma de todos os elementos da lista e cálculo da média
media =sum(entrada)/len(entrada)
# contagem de números positivos e negativos
n = 0
p = 0
for num in entrada:
    if num < 0:
        n+= 1
    elif num > 0:
        p+= 1

print("Média:",media,
      "Positivos:",p,
      "Porcentagem de positivos:",((p/len(entrada))*100),
      "Negativos:",n,
      "Porcentagem de negativos:",((n/len(entrada))*100))