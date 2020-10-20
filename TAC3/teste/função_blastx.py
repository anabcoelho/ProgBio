from Bio.Blast.Applications import *
def blastx (desconhecido, base):

    sequencia = desconhecido
    sequenciasAlvo = base

    meuOutput = "..\\dados\\outputblastx.txt"

    blastx_path = "C:\\Program Files\\NCBI\\blast-2.10.1+\\bin\\blastx"

    ## NcbiblastxCommandline - nucleotideo -> traduz para proteina vs proteina

    linha_de_comando_blastx = NcbiblastxCommandline(cmd=blastx_path,
                                                    query=sequencia,
                                                    subject=sequenciasAlvo,
                                                    outfmt=6,
                                                    out=meuOutput,
                                                    evalue=0.05)

    #
    print("Executando busca local:")

    stdout, stderr = linha_de_comando_blastx()

    print("Fim da busca local...")

sequencia = "..\\dados\\sequenciaDesconhecida.fasta"
sequenciasAlvo = "..\\dados\\tcruzi.fasta"

blastx(sequencia, sequenciasAlvo)