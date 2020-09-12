# Objetivo: Ler arquivo FASTA com apenas um gene e sua sequência. E imprimir o gene e a sequência.
# Variáveis: Entrada: Arquivoin
#            Saída: gene, sequencia
#            De trabalho: cabecalho e linha

Arquivoin = open("C:\\Users\\anabe\\PycharmProjects\\CFB017\\TAC1\\dados"
                  "\\TcCLB.506717.80_mRNA-p1.fasta")

cabecalho = Arquivoin.readline()[1:-1] #ler a 1a linha do arquivo
gene=cabecalho[0:15] #extraindo o gene do cabeçalho
sequencia = "" #abertura da string sequencia

for linha in Arquivoin:
    sequencia += linha.replace('\n','') #append das linhas da sequência

print ("%s\t%s"% (gene,sequencia)) #
Arquivoin.close()



