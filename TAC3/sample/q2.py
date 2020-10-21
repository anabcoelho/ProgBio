#importando bibliotecas
import os
from Bio import SeqIO

#criando pasta de saída
path= '..\\dados\\out2'
os.mkdir(path)


#arquivo de entrada
refArquivoEntrada = open("..\\dados\\TcCLB.506717.80_AA.fasta",'r')

#Dividindo multifasta para fastas
x=1
for i in SeqIO.parse(refArquivoEntrada, "fasta"): #loop
    fname = "..\\dados\\out\\sequencia_%d.fasta" %(x)
    with open(fname, "w") as handle: #escrita
        count = SeqIO.write(i,handle, "fasta")
        #fname.close() #fechar o arquivo recém escrito
    x+=1
print ("done")
refArquivoEntrada.close()
