import pandas as pd
import numpy as np

dataset = pd.read_csv('04_census.csv')

print(type(dataset))

print(dataset)

serie_idade = dataset['age']

print(serie_idade)
print(type(serie_idade))

print(dataset['age'].values, type(dataset['age'].values))

print(serie_idade.head())
print(serie_idade.head(10))

print(serie_idade.tail())
print(serie_idade.tail(10))

# iloc

print(serie_idade.iloc[0])
print(serie_idade.iloc[32551])
print(serie_idade.iloc[-1])

print(serie_idade.iloc[0:3])

print(serie_idade.iloc[[0, 2, 4]])

lista_idade = []
for i in serie_idade.items():
    # print(i)
    # print(i[0], i[1])
    if i[1] > 50:
        lista_idade.append(i[0])  # Aqui ele retorna os indices de cada pessoa

print(lista_idade)
