import numpy as np
import pandas as pd

serie_dados = pd.Series([10, 20, 30, 40, 50])
print(serie_dados)

type(serie_dados)

array_inteiros = [10, 20, 30, 40, 50]
indices = ['A', 'B', 'C', 'D', 'E']
serie_dados = pd.Series(array_inteiros, index=indices)
print(serie_dados)

np_array_inteiros = np.array([10, 20, 30, 40, 50])
print(np_array_inteiros)

type(np_array_inteiros)

serie_dados = pd.Series(array_inteiros)
print(serie_dados)

print(serie_dados.shape)

print(serie_dados.ndim)

print(serie_dados.size)

serie_dados.index = ['A', 'B', 'C', 'D', 'E']

print(serie_dados)

valores = np.random.random(10)
indexes = np.arange(0, 10)
print(valores)
print(indexes)

print(type(valores)), print(type(indexes))

serie_dados = pd.Series(valores, indexes)
print(serie_dados)

print(serie_dados.index)

dicionario = {'Joao': 10, 'Alice': 5, 'Gustavo': 6, 'Pedro': 9}

print(dicionario)

dict_serie_dados = pd.Series(dicionario)
print(dict_serie_dados)
