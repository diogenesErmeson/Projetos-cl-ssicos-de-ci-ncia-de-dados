# Carrega o conjunto de dados chamado de kc_house_data.csv disponível no Kaggle do HD para o projeto
#DAMANDA

#******* EXTRAIR INFORMAÇÕES DE ESTRATÉGICAS PARA TOMADAS DE DECISÃO NUM ESCRITÓRIO DE PROJETOS DE ENGENHARIA QUE
# NEGOCIA IMÓVEIS PELA INTERNET


import pandas as pd

#Testando o arquivo com tuplas e verificando se os quantitativos convergem com os dados do setor de faturamento
data = pd.read_csv('datasets\kc_house_data.csv')

#Mostre as cinco primeiras linhas do conjunto de dados e o cabeçalho
#print(data.head())

#Mostre o numero de colunas e o numeros de linhas do conjunto de dados
#print(data.shape)

#mostre na tela o nome das colunas do conjunto de dados
#print(data.columns)

#mostre na tela o conjunto de dados ordenados pela coluna price
#print(data.sort_values('price'))

#mostre na tela o conjunto de dados ordenados pela coluna preço onde aparece adicionamente o campo id
#print(data[['id','price']].sort_values('price'))

#mostra na tela o conjunto de dados ordenados pela coluna price
#print(data[['id','price']].sort_values('price', ascending=False))

# 1º DEMANDA**************************************************

#   QUAL  A DATA DO IMÓVEL MAIS ANTIGO DO PORTIFOLIO
data['date'] = pd.to_datetime(data['date'])
print(data.sort_values('date', ascending=True))
# R = 02/05/2014

# 2º DEMANDA**************************************************
#   QUANTOS IMÓVEIS POSSUEM O NÚMERO MÁXIMO DE ANDARES?
print(data['floors'].unique())
print(data[data['floors'] == 3.5][['floors','id']])
# R = são 8 imóveis

# 3 DEMANDA**************************************************
#   CLASSIFICAR QUAIS SÃO OS IMOVEIS COM ALTO PADRÃO E BAIXO PADRÃO

data['level'] = 'standard'
data.loc[data['price'] > 540000, 'level'] = 'high_level'
data.loc[data['price'] < 540000, 'level'] = 'low_level'
print(data.head())

# 4 DEMANDA**************************************************
# UM RELATÓRIO COMPLETO DOS IMOVEIS ORDENADO POR PREÇO
report = data[['id','price','date','sqft_lot','bedrooms','level']].sort_values('price', ascending=False)
print(data.head())
report.to_csv('datasets/relatorio.csv', index=False)

# 5 DEMANDA**************************************************
# CRIAR UM MAPA COM A LOCALIZAÇÃO DOS IMÓVEIS A VENDA

import plotly.express as px

data_mapa = data[['id','lat','long','price']]
mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long',
               hover_name='id',
               hover_data=['price'],
               color_discrete_sequence=['fuchsia'],
               zoom=3,
               height=300)

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0, 't':0, 'b':0})
mapa.show()





























