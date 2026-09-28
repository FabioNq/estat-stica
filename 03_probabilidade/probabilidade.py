#%%
# Considerem que S-Espaço Amostral e E-Evento. De modo que, o conjunto E está contido em S. Ainda considerem que o número de resultados favoráveis ao Evento é n(E); e o número de resultados possíveis é n(S) Considerem que Probabilidade: P(E) = N(E) / N(S). Para o lançamento de um dado de 6 faces:
#(1) Calculem a Probabilidade de cada Face do dado; e mostrem que soma de todas as Probabilidades é 1.
#(2) Calculem o Valor Esperado E(X).

#Destarte, repitam os itens (1) e (2) para a SOMA DAS FACES DE DOIS DADOS. Lembre-se que as SOMAS DAS FACES DE DOIS DADOS variam de 2 até 12.

#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

#%%
#criação da matriz 6x6 para colocar todos os resultados possiveis no lançamento de dois dados
combinacoes = np.zeros((6,6))

# insere valor da soma dos lançamentos de dois dados 
for (linha,coluna), elemento in np.ndenumerate(combinacoes):
        elemento = (linha+1)+(coluna+1)
        combinacoes[linha,coluna] = elemento
        
combinacoes

#%%

# pega o maior valor resultante entre a soma dos dois dados 
linhas = int(np.max(combinacoes)) 
#cria uma lista de colunas para colocar dentro do meu dataframe
colunas =['resultados','aparicoes','probabilidade']

# cria uma matriz com valores nulos 12 linhas e 3 colunas
matriz_vazia = np.full((linhas+1,len((colunas))),np.nan)

# cria um dataframe com as linhas preenchidas pela matriz e a lista de colunas
df = pd.DataFrame(matriz_vazia,columns=colunas)
df
#%%
# cria um laço no qual o range é o valor minimo dos resultado da soma de dois dados e o maximo é a maior soma do resultado entre dois dados.
for elementos in range(int(np.min(combinacoes)),int(np.max(combinacoes)+1)):
    # insere a quantidade de aparições de uma determinada soma
    df.iloc[elementos,0] = elementos
    # insere a quantidade de aparições de uma determinada soma    
    df.iloc[elementos,1] = (combinacoes == elementos).sum()
    # calcula a probabilidade de cada resultado de acordo com o espaço amostral
    df.iloc[elementos,2] = df.iloc[elementos,1]/combinacoes.size*100
    print(f"O número {elementos} aparece {df.iloc[elementos,1]} vezes na matriz.")
    print(f"A probabilidade do resultado ser {elementos} é de {df.iloc[elementos,2]:.2f} % ")


#%%
# remove as linhas vazias pois a soma dos dados não resultam nem em 0 e nem em 1.
df_tst = df.dropna()
df_tst
#%%

# cria um grafico de barra resultante nos resultados e na quantidade de vezes que determinado resultado apareceu. 
sns.barplot(
    data=df_tst,
    x="resultados",
    y="aparicoes",
    palette="viridis",
)

