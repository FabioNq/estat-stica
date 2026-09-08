#%%
import pandas as pd 

df = pd.read_excel('pib.xlsx')


#%%
df.info()
#%%
df['PIB per capita'] = df['PIB per capita'].str.rstrip()
df['Número de estabelecimentos de ensino fundamental'] = df['Número de estabelecimentos de ensino fundamental'].str.rstrip()
df['Número de estabelecimentos de ensino médio'] = df['Número de estabelecimentos de ensino médio'].str.rstrip()
df['Pessoal ocupado em postos de trabalho formais'] = df['Pessoal ocupado em postos de trabalho formais'].str.rstrip()



#%%
df.info()
#%%

df = df.astype({'PIB per capita':float,
                'Número de estabelecimentos de ensino fundamental':int, 
                'Número de estabelecimentos de ensino médio': int,
                'Pessoal ocupado em postos de trabalho formais':int })



#%%
percentil_10p = df['PIB per capita'].quantile(0.10)
#%%
df_filtrado_p10 = df[df['PIB per capita'] < percentil_10p]

#%%
df_p10_crescente = df_filtrado_p10.sort_values(by='PIB per capita')

#%%
df_p10_crescente
