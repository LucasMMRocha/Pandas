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

# print(serie_idade_nome.sort_values())

# print(serie_idade_nome.sort_values(ascending=False))

# Ordem alfabetica invertida

# print(serie_idade_nome.sort_index(ascending=False))

sr = serie_idade_nome.sort_values(ascending=False).iloc[0:11]

print(sr)
