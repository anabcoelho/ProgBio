### declarando o uso da biblioteca

from Bio.Seq import Seq
from Bio.SeqUtils import GC, nt_search

### declaro uma sequência que é um objeto da classe Seq usando a string especificada
## O construtor Seq(string_seq) da classe Seq recebe como argumentos uma sequência (string_seq)

stringSeq1 = "ATCGTTGGATGCCACATA"
stringSeq2 = "ATGGTAGGCAGCCACGGC"

sequencia1 = Seq(stringSeq1)
sequencia2 = Seq(stringSeq2)

print("Sequência 1: %s" % sequencia1)
print("Sequência 2: %s" % sequencia2)

##### complemento de um sequência:
# sequência formada por bases que pareiam com as bases da outra fita de DNA, ou seja,
# bases que realizam ligações de hidrogênio na formação da dupla hélice do DNA.
# A pareia com T
# C pareia com G

## método complement() da classe Seq permite esta conversão
complemento_sequencia1 = sequencia1.complement()
complemento_sequencia2 = sequencia2.complement()

print("Complemento da Sequência 1: %s" % complemento_sequencia1)
print("Complemento da Sequência 2: %s" % complemento_sequencia2)

#### se tentar aplicar complement() numa string qualquer:

stringQualquer = "ATCGTTGGATGCCACG"

try:
    print(stringQualquer.complement())
except AttributeError:
    print("Testando complement() em uma string...")
    print("ERRO: complement() é um método da classe Seq!!!")

## Obviamente não vai funcionar, porque a string não tem definida o método complement()!

### complemento reverso de uma sequência:
# A transcrição ocorre em sentidos opostos na fita de DNA

rev_complemento_sequencia1 = sequencia1.reverse_complement()
rev_complemento_sequencia2 = sequencia2.reverse_complement()

print("Complemento reverso da Sequência 1: %s" % rev_complemento_sequencia1)
print("Complemento reverso da Sequência 2: %s" % rev_complemento_sequencia2)


#################### FLUXO DA INFORMAÇÃO GENÉTICA ###########################
#####
#####
################### Transcrição #################
rna_sequencia1 = sequencia1.transcribe()
print("RNA da Sequência 1: %s" % rna_sequencia1)

#################### Transcrição reversa #################

dna2 = rna_sequencia1.back_transcribe()
print("Sequência 1 original\tSequência 1 após transcrição reversa")
print("%s\t%s" %(sequencia1,dna2))

################### Tradução #######################
# Possíveis erros: comprimento da sequência não é múltiplo de 3.
proteina_sequencia1 = sequencia1.translate()
print("Sequência de aminoácidos do RNA de Sequência 1: %s" % proteina_sequencia1)
print("Sequência de aminoácidos da Sequência 1: %s" % sequencia1.translate())

## conteudo GC
print(GC(sequencia1))

## buscando sub-sequencia
print(nt_search(str(sequencia1), "TCGA"))