#%%
import pandas as pd 

df = pd.read_excel('pib.xlsx')


#%%
df.info()
#%%



#df['PIB per capita'] = df['PIB per capita'].str.rstrip()




#%%
df.info()
#%%

df = df.astype({'Mortalidade Infantil':float,
                })



#%%
percentil_10p = df['PIB per capita'].quantile(0.10)
#%%
df_filtrado_p10 = df[df['PIB per capita'] < percentil_10p]

#%%
df_p10_crescente = df_filtrado_p10.sort_values(by='PIB per capita')

#%%
df_p10_crescente

#%%

df_p10_crescente_corr = df_p10_crescente.select_dtypes(include ='float')

matriz_correlacao = df_p10_crescente_corr.corr()
print(matriz_correlacao)