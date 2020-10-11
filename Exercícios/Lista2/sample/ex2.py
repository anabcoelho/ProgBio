# Programa que pede ao usuário uma sequência de aminoácido e imprima o percentual de cada aminoácido.

seq = str(input('Sequência de AA:')).upper() #entrada: upper para deixar todos com letras maiúsculas

total = len(seq) #numero total de aminoácidos

#Dicionário de contagem de aminoácidos
count = { 'A': 0, 'C': 0, 'D' : 0,'E' : 0,'F' : 0,'G' : 0,'H' : 0,'I' : 0,'K' : 0,'L' : 0,'M' : 0,
'N' : 0,'P' : 0,'Q' : 0,'R' : 0,'S' : 0,'T' : 0,'V' : 0,'W' : 0,'Y' : 0}

# contagem pra cada aminoácido
for i in seq:
    count[i]+=1 # a cada item que tiver no count adiciona mais 1 a contagem

# porcentagem
for key, value in count.items(): # para cada aa e valores no dicionário em uma lista de tuplas com os pares (aa,valores)
    if value != 0: #se contém o AA
       por = float((value/total)*100) #calculo da %
       print(key, por) #imprimir o AA e sua porcentagem