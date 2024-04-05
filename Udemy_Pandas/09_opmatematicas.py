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


print(serie_pais)

print(serie_pais + 2)

print(serie_pais.add(2))

print(serie_pais.sub(2))

print(serie_pais.mul(2))

print(serie_pais.div(2))

s1 = pd.Series([20, 30, 40])
s2 = pd.Series([1, 2, 3])
print(s1, s2)

print(s1.add(s2))

print(s1.sub(s2))

print(s1.mul(s2))

print(s1.div(s2))
