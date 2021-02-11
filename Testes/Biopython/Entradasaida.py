###### Lendo um arquivo FASTA com uma única sequência

from Bio import SeqIO

refArquivoEntrada1 = open("..\\data\\TcCLB.506717.80_AA.fasta", "r")


for i in SeqIO.parse(refArquivoEntrada1, "fasta"):

    # imprime o cabecalho
    print(i.id)

    # imprime a sequencia
    print(i.seq)

    # imprime o tamanho da sequencia
    print(len(i))




########## escrevendo um arquivo com proteinas onde:
# a) comprimento maior que 2000
# b) primeiro aminoácido é uma metionina
# c)imprima também o identificador e a sequencia separada por tabulacao

refArquivoEntrada = open("..\\data\\TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta", "r")
refArquivoSaida = open("..\\data\\TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins_maiorQue2000AA.fasta", "w")

### parse do arquivo multi-FASTA
for i in SeqIO.parse(refArquivoEntrada, "fasta"):

    ## testa se o comprimento é maior que 2000 aminoácidos
    ## e se o primeiro aminoácido da sequência é uma metionina.

    if ((len(i.seq) > 2000) and (i.seq[0] == 'M')):
        ## escreve o identificador id e a sequência seq na tela
        print("%s\t%s" % (i.id, i.seq))

        ## cada objeto i é relativo a classe Seq
        ## a cada iteração seus atributos são escritos no arquivo refArquivoSaida
        ## no formato definido "fasta"
        SeqIO.write(i, refArquivoSaida, "fasta")

refArquivoEntrada.close()
refArquivoSaida.close()