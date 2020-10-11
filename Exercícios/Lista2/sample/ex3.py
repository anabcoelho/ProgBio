#peça ao usuário duas sequências de DNA e imprima o complemento reverso de sua concatenação
# seq1 e seq2: sequências do usuário; seq: concatenação da sequência; rseq: sequência reversa;
# complementor: complemento reverso.

# entrada das sequências
seq1 = str(input('Sequência 1:'))
seq2 = str(input('Sequência 2:'))

seq = seq1 + seq2 # concatenando as sequências
rseq = seq[::-1] #Invertendo seq

complementor = '' #inicio do complemento reverso

for i in rseq:
    if i.upper() == 'A': ## A passa a ser T
        complementor+='T'
    if i.upper() == 'T': ## T passa a ser A
        complementor+='A'
    if i.upper() == 'G':## G passa a ser C
        complementor+='C'
    if i.upper() == 'C': ## C passa a ser G
        complementor+='G'

print(complementor)