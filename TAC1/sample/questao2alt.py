# Objetivo: Ler arquivo multi-FASTA com vários genes e suas sequência. E imprimir o cabeçalho e a sequência.
# Variáveis: Entrada: refArquivo
#            Saída: cabecalho, sequencia
#            De trabalho: linha, v
refArquivo = open("C:\\Users\\anabe\\PycharmProjects\\CFB017\\TAC1\\dados"
                  "\\TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta")
cabecalho=''
sequencia= ''
v=1 #variavel que indica que é a primeira sequência

for linha in refArquivo:
    if v==1: # indica que é a 1o cabeçalho
        cabecalho = linha
        print('Cabeçalho: %s' % cabecalho)  # Cabeçalho atual
        v=2 # 2a linha em diante
    else: # 2a linha em diante
        if linha [0] == ">":
            cabecalho = linha
            print('Sequência: %s \n' %sequencia) #sequencia anterior (já na mesma linha)
            print('Cabeçalho: %s' % cabecalho) #Cabeçalho atual
            sequencia = "" #zerar a sequência atual
        else:
            sequencia += linha.replace('\n','')  #append das linhas da sequência

print('Sequência: %s' %sequencia) #última sequencia
refArquivo.close()




