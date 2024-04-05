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

print(serie_idade_nome.value_counts())

serie_idade_nome.value_counts(bins=10)
