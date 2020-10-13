from Bio.Blast.Applications import *

### endereço completo para os arquivos

sequencia = "..\\data\\TcCLB.506717.80_AA.fasta"
sequenciasAlvo = "..\\data\\TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta"
meuOutput = "..\\data\\out.blastp.outfmt6.txt"

blastp_path = "C:\\Program Files\\NCBI\\blast-2.10.1+\\bin\\blastp"

## criando a linha de comando para o blastp (proteína vs proteína)

## NcbiblastpCommandline - proteina vs proteina
## NcbiblastnCommandline - nucleotideo vs nucleotideo
## NcbiblastxCommandline - nucleotideo -> traduz para proteina vs proteina

linha_de_comando_blastp = NcbiblastpCommandline(cmd=blastp_path, query=sequencia, subject=sequenciasAlvo, outfmt=6, out=meuOutput, evalue=0.05)

print("A linha de comando para o blastp é:\n%s" % linha_de_comando_blastp)

#
print("Executando busca local:")

stdout, stderr = linha_de_comando_blastp()

print("Fim da busca local...")

# Abrindo resultado
blast_result = open(meuOutput, "r")

##### indíces para os resultados do blast em formato 6 ("outfmt=6")

qseqid = 0 #query (e.g., unknown gene) sequence id
sseqid = 1 # subject (e.g., reference genome) sequence id
pident = 2 # percentage of identical matches
length = 3 # alignment length (sequence overlap)
mismatch = 4 # number of mismatches
gapopen = 5 # number of gap openings
qstart = 6 # start of alignment in query
qend = 7 # end of alignment in query
sstart = 8 # start of alignment in subject
send = 9 # end of alignment in subject
evalue = 10 # expect value
bitscore = 11 # bit score

results = blast_result.read()
s = results.split('\n')

for linha in s:
    hit = linha.split('\t')
    print(linha)

    if len(hit) != 12:
        break

    print("Sequência de busca: %s" % hit[qseqid])
    print("Sequência encontrada: %s" % hit[sseqid])
    print("Score = %s" % hit[bitscore])
    print("Identidade = %s" % hit[pident])
    print("E-value = %s" % hit[evalue])
    print("________________________________________________")