### declarando o uso da biblioteca

from Bio.Seq import Seq

### declaro uma sequência que é um objeto da classe Seq usando a string especificada
## O construtor Seq(string_seq) da classe Seq recebe como argumentos uma sequência (string_seq)

stringSeq1 = "ATCGTTGGATGCCACATA"
stringSeq2 = "ATGGTAGGCAGCCACGGC"
stringSeq3_igual_a_seq1 = "ATCGTTGGATGCCACATA"

sequencia1 = Seq(stringSeq1)
sequencia2 = Seq(stringSeq2)
sequencia3 = Seq(stringSeq3_igual_a_seq1)

print("Sequência 1: %s" % sequencia1)
print("Sequência 2: %s" % sequencia2)
print("Sequência 3: %s" % sequencia3)

### verificando os objetos

if not isinstance(sequencia1,str):
    print("Objeto sequencia1 não é uma instância ou objeto da classe String")
else:
    print("Objeto sequencia1 é uma instância ou objeto da classe String")

if isinstance(sequencia1,Seq):
    print("Objeto sequencia1 é uma instância ou objeto da classe Seq")
else:
    print("Objeto sequencia1 não é uma instância ou objeto da classe Seq")

######### Operações com Sequências

#### concatenação

sequencia_concatenada = sequencia1 + sequencia2

print("Sequência concatenada: %s" % sequencia_concatenada)
print("Sequência concatenada transcrita: %s" % sequencia_concatenada.transcribe())

#### comparação

if str(sequencia1) == str(sequencia2):
    print("Sequência 1 é igual à Sequência 2")
else:
    print("Sequência 1 é diferente da Sequência 2")

if str(sequencia1) == str(sequencia3):
    print("Sequência 1 é igual à Sequência 3")
else:
        print("Sequência 1 é diferente da Sequência 3")