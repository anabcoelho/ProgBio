import sys
l= sys.argv
excel= l[1]
b= float(l[2])
m= float (l[3])
import pandas as pd
#arqout= open ('..\\dados\\saida.out', 'w')
#b=58.53223295
#m=-3.97186047
#with pd.ExcelFile ('..\\dados\\Valores_CT.xlsx') as xlsx:
    #df = pd.read_excel(xlsx)
with pd.ExcelFile(excel) as xlsx:
    df = pd.read_excel(xlsx)


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
df.to_csv (r'..\\dados\\saida.csv', index = False, header=True)
