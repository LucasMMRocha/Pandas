import pandas as pd
import numpy as np
from faker import Faker

dataset = pd.read_csv('04_census.csv')
serie_idade = dataset['age']

fake = Faker()

fake.name()

indices_nome = []

for i in range(32561):
    indices_nome.append(fake.name())

serie_idade_nome = pd.Series(np.array(dataset['age']), index=indices_nome)

fake.country()

indices_pais = []
for _ in range(32561):
    indices_pais.append(fake.country())

print(indices_pais[0:11])

serie_pais = pd.Series(np.array(dataset['age']), index=indices_pais)

print(serie_pais)

print(serie_pais.loc[serie_pais > 50])

print(serie_pais.loc[(serie_pais > 50) & serie_pais.index == "India"])

