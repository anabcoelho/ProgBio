# importação de biblioteca:
from Bio.Seq import Seq

#input
entrada= str(input('insira a sequência de DNA:'))
DNA = Seq(entrada)

#Transcrição
mRNA = DNA.transcribe()

# Tradução
ptn = mRNA.translate()

#imprimir
print('mRNA:', mRNA)
print('ptn:', ptn)