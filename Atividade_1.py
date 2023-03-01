#lista de exercicios
import pandas as pd

data = pd.read_csv('datasets\kc_house_data.csv')

# 1 - QUANTAS CASAS ESTÃO DISPONIVEIS PARA COMPRA
print(len(data))

# 2 - Quantos atributos as casas possuem
print(len(list(data)))

#3 - Quais são os atributos das casas
print(data.columns)

#4 - Qual a casa mais cara(casa com o maior valor de venda?)

#print(max(data['price']))
print(data[['id','price']].sort_values('price',ascending=False))

# 5 - Qual a casa com o maior número de quartos
print(data['bedrooms'].unique())
print(data[['id','bedrooms']].sort_values('bedrooms',ascending=False))

# 6 - A soma total do numero de quartos
print('A soma com o número de quartos: ', data['bedrooms'].sum())

# 7 - Quantas casas possuem dois banheiros
#print(data['bathrooms'].unique())
print('Numero de imoveis com somente dois banheiros: ', data[data['bathrooms']==2].shape)

# 8 - Qual o preço médio de todas as casas do conjunto de dados.
print(data['price'].mean())

# 9 - Qual o preço médio de casas com dois banheiros
print('preço médio de casas com 2 banheiros: ',data.loc[data['bathrooms']==2,'price'].mean())

# 10 - Qual o preço médio de casas com 3 quartos
print('preço médio de casas com 3 quartos: ',data.loc[data['bedrooms'] == 3, 'price'].mean())

# 11 - Quantas casas possuem mais de trezentos metros
#print(data.loc[data['price'] > 540000, )











