import pandas as pd
import numpy as np

valores = np.random.random(10)
indexes = np.arange(0, 10)

dicionario = {'Joao': 10, 'Alice': 5, 'Gustavo': 6, 'Pedro': 9}
dict_serie_dados = pd.Series(dicionario)

serie_dados = pd.Series(valores, indexes)

# serie_dados2 = serie_dados --> Nao fazer assim, pois dessa forma uma esta relacionada a outra

serie_dados2 = serie_dados.copy()

print(serie_dados2.dtype)

print(serie_dados2.astype(int))

print(serie_dados2.dtype) # Perceba que aqui o tipo ainda e float. Para mudar isso devemos atribuir uma nova variavel

s3 = serie_dados2.astype(int)

print(s3.dtype)

dados_novos = {'Gustavo': 20, 'Alana': 30}
serie_dados3 = pd.Series(dados_novos)
print(serie_dados3)

print(dict_serie_dados)

serie_dados4 = pd.concat([dict_serie_dados, serie_dados3])
print(serie_dados4)

