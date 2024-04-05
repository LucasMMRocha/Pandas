import pandas as pd
import numpy as np
from faker import Faker

dataset = pd.read_csv('04_census.csv')
serie_idade = dataset['age']

print(serie_idade)

print(serie_idade.loc[serie_idade < 18])


def corrige_idade(idade):
    if idade < 18:
        idade = 18
    return idade

# print(corrige_idade(20))
# print(corrige_idade(17))


serie_idade = serie_idade.apply(corrige_idade)

print(serie_idade.loc[serie_idade < 18])

serie_idade = serie_idade.apply(lambda x: 17 if x == 18 else x)

print(serie_idade.loc[serie_idade < 18])

serie_idade2 = serie_idade.iloc[0:6]
print(serie_idade2)

print(serie_idade2.where(serie_idade2 < 40, 0))
