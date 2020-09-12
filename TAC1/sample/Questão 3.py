import csv # importar a biblioteca csv
#Abrindo ariquivo na variável f.
with open("C:\\Users\\anabe\\PycharmProjects\\CFB017\\TAC1\\dados\\species.csv") as f:
    reader = csv.reader(f) #leitura do arquivo CSV
    for row in reader:
         if row[3].upper().rstrip() == "BIRD": #se na coluna 3 tem bird (escrito de qualquer maneira)
            print (row)