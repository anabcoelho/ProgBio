import sys
print (sys.argv)
#gera lista com nome do arquivo + argumentos em strings

num_args = len(sys.argv)
print("Total de argumentos: %d" % num_args)

for i in range(num_args):
    print("Argumento %d com índice %d = %s" % (i+1,i,sys.argv[i]))

if num_args < 3:
    print("Você precisa digitar dois números como argumentos. Finalizando script.")
    sys.exit()
