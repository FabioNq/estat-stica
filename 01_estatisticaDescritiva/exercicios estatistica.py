#%%
import pandas as pd 
import numpy as np 
from scipy import stats
#%%

lista = np.array([12,18,33,57,12])

def media(lista):
    return np.mean(lista)

def mediana(lista):
    return np.median(lista)

def moda(lista):
    return stats.mode(lista)

def desvio(lista):
    return np.std(lista)


#%%
print(media(lista))
#%%
print(mediana(lista))
#%%
print(moda(lista))

#%%
print(desvio(lista))


#%% 
#Erro Quadrado Media
consolidadoMedia = 0
mediaGeral = media(lista)
for i in lista:
    calculo = (i - mediaGeral)**2
    consolidadoMedia += calculo
print(consolidadoMedia)
z = desvio(lista)

#%%
#Erro Quadrado Mediana 
consolidadeMediana = 0
medianaGeral = mediana(lista)
for i in lista:
    calculo = (i - medianaGeral)**2
    consolidadeMediana += calculo
print(consolidadeMediana)
desviomediana = desvio(medianaGeral)




#%%
#Erro Quadrado Moda
consolidadoModa = 0
modaGeral = moda(lista).mode
for i in lista:
    calculo = (i - modaGeral)**2
    consolidadoModa += calculo
print(consolidadoModa)

desvioModa = desvio(modaGeral)


#%%
df_consolidado = pd.DataFrame({
    'index':[0],
    'varianciaMedia': consolidadoMedia,
    'varianciaMediana': consolidadeMediana,
    'varianciaModa': consolidadoModa,
    'desvioPadraoMedia': z,
    'desvioPadraoMediana': desviomediana,
    'desvioPadraoModa' : desvioModa
})


df_consolidado.head()