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

# print(indices_nome)

print(type(indices_nome), len(indices_nome))

print(indices_nome[0:10])

print(serie_idade.size)

serie_idade_nome = pd.Series(np.array(dataset['age']), index=indices_nome)

print(serie_idade_nome)

serie_idade_nome2 = serie_idade_nome.drop_duplicates()
print(serie_idade_nome2.size)

print(serie_idade_nome2)

print(serie_idade_nome2.loc['Andrea Henderson':'Kimberly Nelson'])
