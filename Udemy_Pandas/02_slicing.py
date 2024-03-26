import pandas as pd
import numpy as np

valores = np.random.random(10)
indexes = np.arange(0, 10)

serie_dados = pd.Series(valores, indexes)

print(serie_dados[:])

print(serie_dados[0:3])

print(serie_dados[0:4])

print(serie_dados[:4])

print(serie_dados[-1:])

print(serie_dados[:-1])

s2 = serie_dados[:3]

print(s2)
