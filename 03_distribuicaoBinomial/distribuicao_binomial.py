# Exemplo 
# Em oito lançamentos de uma moeda, qual é a probabilidade de se obter 3 caras? Calcular o Valor Esperado e a Variância?


#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import math



#%%
colunas =['totalCara','probabilidade','valorEsperado','variancia']

df = pd.DataFrame(columns=colunas)
df
#%%


def distribuicaoBinomial(n,x,p):
    
    global df
    
    nf = math.factorial(n)
    xf = math.factorial(x)
    fat = nf/(xf*math.factorial(n-x))
    bin = fat*(p**x)*(1-p)**(n-x)
    df['valorEsperado'] = n*p
    df['variancia'] = n*p*(1-p)
    return bin



#%%
for i in range(8):
    df.loc[i,'totalCara'] =  i
    df.loc[i,'probabilidade'] = distribuicaoBinomial(8,i,0.5)
    
    
    
#%%    
df



#%%

sns.barplot(
    data=df,
    x="totalCara",
    y="probabilidade",
    palette="viridis",
)
