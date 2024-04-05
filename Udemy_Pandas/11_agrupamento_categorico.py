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

serie_pais_index = serie_pais.index.to_series()

serie_pais_index.reset_index(drop=True, inplace=True)
print(serie_pais_index)

print(serie_pais_index.value_counts())

print(serie_pais_index.value_counts(normalize=True))

print(serie_pais_index.unique())

print(serie_pais_index.nunique())
