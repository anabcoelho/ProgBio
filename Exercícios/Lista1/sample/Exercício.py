import pandas as pd
filelocation = '..\\dados\\WHOTB.xlsx'
df = pd.read_excel(filelocation)
print(df)
print (' Número de mortos %d' % df ['TB deaths'].sum ())
print (' Máximo de mortos %d' % df ['TB deaths'].max ())
print (' Mínimo de mortos %d' % df ['TB deaths'].min ())
print (' Média de mortos %d' % df ['TB deaths'].mean ())
print (' Mediana de mortos %d' % df ['TB deaths'].median ())
dataord= df.sort_values('TB deaths')
print ('Ordenando de maneira crescente: \n %s ' %dataord)
datanorm=dataord
datanorm['TB deaths'] = datanorm['TB deaths']/100000 # nomalizando

print( 'Ordenado e Normalizado \n %s' %datanorm)
# BRICS
#só consegui dessa forma
#crei um dicionário (dic) com o b,r,i,c,s e mandei pd.dataframe(dic)

b=df.loc[df['Country'] == "Brazil"]
soma= int(b['TB deaths'])
r=df.loc[df['Country'] == "Russian Federation"]
soma= int(r['TB deaths'])
i=df.loc[df['Country'] == "India"]
soma= soma+ int(i['TB deaths'])
c=df.loc[df['Country'] == "China"]
soma= soma+ int(c['TB deaths'])
s=df.loc[df['Country'] == "South Africa"]
soma= soma+ int(s['TB deaths'])

print("Numero de mortos dos BRICS: %d" %soma)