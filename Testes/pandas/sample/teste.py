import pandas as pd
import csv
#não consegui de jeito nenhum ir pelo xlrd
#with pd.ExcelFile('..\\Lista1\\dados\\WHOTB.xlsx') as xlsx:
    #df = pd.read_excel(xlsx, 'Counts')
with open('/Exercícios/Lista1\\dados\\WHOTB.csv') as f:
    reader = csv.reader(f) #leitura do arquivo CSV