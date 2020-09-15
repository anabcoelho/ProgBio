# Objetivo: Ler arquivo multi-FASTA com vários genes e suas sequência. E imprimir o cabeçalho e a sequência.
# Variáveis: Entrada: refArquivo
#            Saída: cabecalho, sequencia
#            De trabalho: linha
refArquivo = open("C:\\Users\\anabe\\PycharmProjects\\CFB017\\TAC1\\dados"
                  "\\TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta")
cabecalho=''
sequencia= ''

for linha in refArquivo:
    if linha [0] == ">":
        if sequencia != "":
            print('Cabeçalho: %s' % cabecalho) #Cabeçalho atual
            print('Sequência: %s \n' % sequencia)  # sequencia anterior (já na mesma linha)
            cabecalho = linha
            sequencia = "" #zerar a sequência atual
    else:
        sequencia += linha.replace('\n','')  #append das linhas da sequência
refArquivo.close()