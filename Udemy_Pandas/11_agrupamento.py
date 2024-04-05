import pandas as pd
import numpy as np
from faker import Faker

dataset = pd.read_csv('04_census.csv')
serie_idade = dataset['age']

fake = Faker()

fake.country()

indices_pais = []
for _ in range(32561):
    indices_pais.append(fake.country())

serie_pais = pd.Series(np.array(dataset['age']), index=indices_pais)

print(serie_pais.sum())

print(serie_pais.mean())

print(serie_pais.median())

print(serie_pais.count())

print(serie_pais.std())

print(serie_pais.var())

print(serie_pais.loc["Brazil"].mean())

print(serie_pais.quantile([0.25, 0.5, 0.75]))
