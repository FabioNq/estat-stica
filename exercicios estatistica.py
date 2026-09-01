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

#%%
print(media(lista))
#%%
print(mediana(lista))
#%%
print(moda(lista))