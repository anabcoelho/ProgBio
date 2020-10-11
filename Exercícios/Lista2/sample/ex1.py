##recebe uma sequência de DNA do usuário e calcula o conteúdo GC da sequência.
## Variáveis: seq (input do usuário), count: contagem de GC, GC: conteúdo GC= (C+G)*100/tamanho da sequência
seq = str(input('Sequência de nucleotídeos:')) ## entrada

# contador de GC
count = 0
for i in seq:

    if str(i).upper() == "G" or str(i).upper() == "C" :
        count = count+1

GC=(count*100)/len(seq)

print('total = ', len(seq))
print('GC = ', GC)