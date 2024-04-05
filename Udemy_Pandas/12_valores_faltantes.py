import pandas as pd
import numpy as np

serie_faltante = pd.Series([1, 2, 3, np.nan, 5, np.nan])
print(serie_faltante)

print(serie_faltante.isna())

print(serie_faltante.isna().sum())

print(serie_faltante.value_counts())

print(serie_faltante.value_counts(dropna=False))

print(serie_faltante.fillna(0))

print(serie_faltante.dropna())

print(serie_faltante.fillna(serie_faltante.mean()))

serie_faltante = pd.Series(["Maca", "Banana", "Arroz", "Arroz", np.nan, "Batata"])
print(serie_faltante)

print(serie_faltante.isna().sum())

print(serie_faltante.fillna("Nao informado"))

print(serie_faltante.mode())

print(serie_faltante.mode().iloc[0])

print(serie_faltante.fillna(serie_faltante.mode().iloc[0]))
