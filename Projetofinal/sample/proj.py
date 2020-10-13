# importand pacotes
import sys



# importando dados da linha de comando

# Ler xlsx

# Importando fastas

#criando novas colunas

fatorNormalizacao_Rep1_CondA = 10**6/df['Rep1_CondA_Counts'].sum()
fatorNormalizacao_Rep2_CondA = 10**6/df['Rep1_CondA_Counts'].sum()
fatorNormalizacao_Rep1_CondB = 10**6/df['Rep1_CondB_Counts'].sum()
fatorNormalizacao_Rep2_CondB = 10**6/df['Rep2_CondB_Counts'].sum()

data_normalizado = {
    'gene' : df['gene'],
    'Rep1_CondA_CPM': df['Rep1_CondA_Counts']*fatorNormalizacao_Rep1_CondA,
    'Rep2_CondA_CPM': df['Rep2_CondA_Counts']*fatorNormalizacao_Rep2_CondA,
    'Rep1_CondB_CPM': df['Rep1_CondB_Counts']*fatorNormalizacao_Rep1_CondB,
    'Rep2_CondB_CPM': df['Rep2_CondB_Counts']*fatorNormalizacao_Rep2_CondB
}

df_normalizado = pd.DataFrame(data_normalizado, columns=['gene','Rep1_CondA_CPM','Rep2_CondA_CPM','Rep1_CondB_CPM','Rep2_CondB_CPM'])

print("Maior de valor expressão por réplica depois da normalização:")
print(df_normalizado.max(numeric_only=True).sort_values(ascending=False))