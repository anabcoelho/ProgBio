from Bio.Blast.Applications import *
### endereço completo para os arquivos

#sequencia = "..\\dados\\sequenciaDesconhecida.fasta"
#sequenciasAlvo = "..\\dados\\tcruzi.fasta"
#meuOutput = "..\\dados\\outputblastx.txt"

def blastx (sequencia, sequenciasAlvo, outputlocal):
    blastx_path = "C:\\Program Files\\NCBI\\blast-2.10.1+\\bin\\blastx"
    ## NcbiblastxCommandline - nucleotideo -> traduz para proteina vs proteina
    linha_de_comando_blastx = NcbiblastxCommandline(cmd=blastx_path,
                                                query=sequencia,
                                                subject=sequenciasAlvo,
                                                outfmt=6,
                                                out=outputlocal,
                                                evalue=0.05)

    #
    print("Executando busca local:")

    stdout, stderr = linha_de_comando_blastx()

    print("Fim da busca local...")

    # Abrindo resultado
    blast_result = open(meuOutput, "r")
##### indíces para os resultados do blast em formato 6 ("outfmt=6")

    qseqid = 0 #query  sequence id
    sseqid = 1 # subject  ptn id
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
    bitanterior=1.0
    for linha in s:
        hit = linha.split('\t')
        if len(hit) != 12:
             break
        bit = hit[bitscore]
        bit=float (bit)
        if bitanterior < bit:
            maxi=hit
            bitanterior = bit
    print("Sequência de busca: %s" % maxi[qseqid])
    print("Sequência encontrada: %s" % maxi[sseqid])
    print("Score = %s" % maxi[bitscore])
    print("Identidade = %s" % maxi [pident])
    print("E-value = %s" % maxi [evalue])
    print("________________________________________________")
    return maxi

maximo= blastx(sequencia,sequenciasAlvo, meuOutput)
print(maximo)
