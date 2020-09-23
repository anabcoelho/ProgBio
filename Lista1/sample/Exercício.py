import pandas as pd
filelocation = '..\\dados\\WHOTB.xlsx'
df = pd.read_excel(filelocation)
print(df)
print (' Número de mortos %d' % df ['TB deaths'].sum ())
print (' Máximo de mortos %d' % df ['TB deaths'].max ())
print (' Mínimo de mortos %d' % df ['TB deaths'].min ())
print (' Média de mortos %d' % df ['TB deaths'].mean ())
print (' Mediana de mortos %d' % df ['TB deaths'].median ())
print ('Ordenando de maneira crescente: \n %s ' %df.sort_values('TB deaths'))
Norm = df['TB deaths']/
print(Norm)
data_normalizado =
print(data_normalizado)
