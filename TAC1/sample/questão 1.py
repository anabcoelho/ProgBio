Arquivoin = open("C:\\Users\\anabe\\PycharmProjects\\CFB017\\TAC1\\dados"
                  "\\TcCLB.506717.80_mRNA-p1.fasta")

cabecalho = Arquivoin.readline()[1:-1]
gene=cabecalho[0:15]
sequencia = ""
for linha in Arquivoin:
    sequencia += linha.replace('\n','')

print ("%s\t%s"% (gene,sequencia))
Arquivoin.close()



