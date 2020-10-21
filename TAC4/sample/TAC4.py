#Importando bibliotecas
from Bio import SeqIO

sequencia= str(input("Digite sua sequência:").upper()) # sequencia em letras maiúsculas

#abrindo multifasta

multifasta=open("..\\data\\multifastatcruzi.fasta", 'r')

#procurar no multifasta
Y=0 #numero de vezes que a sequencia apareceu
for i in SeqIO.parse(multifasta, "fasta"):
    #i.seq é uma string com as sequencias de aa ou nucleotídeos
    x= i.seq.count(sequencia) # se tem o motivo na proteína/DNA será um número maior que zero
    if x > 0:
        print (i.id)
        Y=Y+x #contagem do y

print("done")
print("O numero de vezes que %s aparece é:" %sequencia, Y)