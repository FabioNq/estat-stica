#%%
import pandas as pd 

df = pd.read_excel('municipios_rn_pib_per_capita.xlsx')



#%%
df
#%%
percentil_10p = df['PIB Per Capita (R$)'].quantile(0.10)

#%%

df_filtrado_p10 = df[df['PIB Per Capita (R$)'] < percentil_10p]



#%%

df_p10_crescente = df_filtrado_p10.sort_values(by='PIB Per Capita (R$)')

#%%
df_p10_crescente