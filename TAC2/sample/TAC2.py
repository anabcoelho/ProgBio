
import sys
import pandas as pd

l= sys.argv # Entrada: arquivo m b
excel= l[1]
m= float(l[2])
b= float (l[3])


with pd.ExcelFile(excel) as xlsx: #leitura arquivo
    df = pd.read_excel(xlsx)

#Normalizando...
fatornorm = 10** (df['CT']-b)/m

data_q = {
    'Target_Name' : df['Target_Name'],
    'Stage' : df['Stage'],
    'Quantity': fatornorm,
}

df_q = pd.DataFrame(data_q, columns=['Target_Name','Stage','Quantity'])

Qt=df_q['Quantity']

df_final= df

df['Quantity'] = Qt

print (df_final)

df.to_csv (r'..\\dados\\saida.csv', index = False, header=True) #saída para CSV
