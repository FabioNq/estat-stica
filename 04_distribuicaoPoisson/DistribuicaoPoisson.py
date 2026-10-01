#%%
import pandas as pd
import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

#%%
colunas =["valorX","probabilidade"]

df = pd.DataFrame(columns=colunas)


df

df_halland = df

#%%
#Calcular probabilidade de se obter 1 chamada em 90 minutos, em um telefone que recebe
#em media 2 chamadas por hora ?

# X = 1
# t = 2 chamadas em 60 minutos t chamadas em 90 minutos = 3

x = 1
t = (2*90)/60
print(f'valor de {x} e valor de {t}')





#%%

for i in range(17):
    global df
    df.loc[i,"valorX"] = i 
    df.loc[i,"probabilidade"] = poisson.pmf(i,t)
#%%
df


#%%
plt.bar(df['valorX'], df['probabilidade'], color='blue')
plt.title('total de chamadas por hora')
plt.xlabel('Chamadas')
plt.ylabel('probabilidade de chamadas por hora')
plt.show()





#%%
# quantidade de gols Halland esperados em 90 minutos
#%%

for i in range(6):
    global df_halland
    df_halland.loc[i,"valorX"] = i 
    df_halland.loc[i,"probabilidade"] = poisson.pmf(i,0.86)
#%%
plt.bar(df_halland['valorX'], df_halland['probabilidade'], color='blue')
plt.title('probabilidade de Gols do Halland em 90min')
plt.xlabel('total de gols')
plt.ylabel('probabilidade de gols')
plt.show()




#%%
df_halland