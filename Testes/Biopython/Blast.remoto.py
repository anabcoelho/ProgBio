### realizando busca remota usando BLAST

from Bio.Blast import NCBIWWW
from Bio import SeqIO

minhaEntradaFasta = SeqIO.read("/home/vitor/PycharmProjects/VitorCoelho/Biopython/data/TcCLB.506717.80_AA.fasta", format="fasta")

print("Iniciando busca remota no NCBI..." )

resultadoBuscaBlast = NCBIWWW.qblast("blastp", "nr", minhaEntradaFasta.seq, format_type="Text",expect=0.05, hitlist_size=10)

print(resultadoBuscaBlast.read())

print("Fim da busca no no NCBI..." )