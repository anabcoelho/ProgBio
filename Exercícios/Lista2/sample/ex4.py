# usuario sequência de DNA que contém dois exons e um íntron;
#leia do usuário as coordenadas do primeiro exon (start1;end1) e do segundo exon (start2;end2).
#imprimir a região exônica (as sub-sequências concatenadas do primeiro exon com o segundo exon).

DNA = str(input('Digite sua sequência de DNA:')) #entrada da sequência do DNA

# recebendo coordenadas e arrumando-as
## o split separa o input e gera uma lista com os itens que foram separados
coordenada1 = str(input('coordenada 1: (no formato: x;y)'))
coordenada2 = str(input('coordenada 2: (no formato: x;y)'))
#Separando os itens com split(), gerando uma lista com as stings das coordenadas
coordenada1= coordenada1.split(";")
coordenada2= coordenada2.split(";")
# transformando em numero e deve-se subtrair -1 das coordenadas
start1=int(coordenada1[0])-1
end1=int(coordenada1[1])-1
start2=int(coordenada2[0])-1
end2=int(coordenada2[1])-1

#fatiando
exon1 = DNA[start1:end1] #fatiando somente a parte do exon 1
exon2 = DNA[start2:end2] #fatiando somente a parte do exon 2

#concatenação
exon = exon1+exon2
print(exon)