import sys
import pandas as pd
arqout= open ('..\\dados\\saida.out', 'w')
b=58.53223295
m=-3.97186047
with pd.ExcelFile('..\\dados\\Valores_CT.xlsx') as xlsx:
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
strdf_final= str(df_final)
arqout.write(strdf_final)

## Está imprimindo assim:
#Sample_Name Target_Name  Stage     CT      Quantity
#0      CondA_1       RNA_1  CondA  15.26 -1.345157e-44
#1      CondA_2       RNA_1  CondA  18.29 -1.441362e-41
#2      CondA_3       RNA_1  CondA  17.15 -1.044174e-42
#3      CondB_1       RNA_1  CondB  19.97 -6.898792e-40
#4      CondB_2       RNA_1  CondB  18.38 -1.773263e-41
#..         ...         ...    ...    ...           ...
#67     CondC_2       RNA_6  CondC  28.54 -2.563144e-31
#68     CondC_3       RNA_6  CondC  28.85 -5.233269e-31
#69     CondD_1       RNA_6  CondD  19.04 -8.105374e-41
#70     CondD_2       RNA_6  CondD  19.65 -3.301970e-40
#71     CondD_3       RNA_6  CondD  20.04 -8.105374e-40
# e o arquivo de saída está saindo do mesmo jeito