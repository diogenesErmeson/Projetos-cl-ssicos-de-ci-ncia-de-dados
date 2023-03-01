# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from numpy import int64


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pandas as pd

data = pd.read_csv('datasets\kc_house_data.csv')

#mostra os tipos de variáveis do arquivo
#print(data.dtypes)


#data['date'] = pd.to_datetime(data['date'])
#print(data.dtypes)

#converter inteiro -> float
#data['bedrooms'] = data['bedrooms'].astype(float)
#print(data.dtypes)

#converter de float -> inteiro
#data['bedrooms'] = data['bedrooms'].astype(int64)
#print(data.dtypes)

#converter de um inteiro-> string
#data['bedrooms'] = data['bedrooms'].astype(str)

"""
MINIPULAR AS VARIAVEIS
-criar (COLUNAS DE VARIAVEIS E NOVAS COLUNAS
-Deletar (colunas de variaveis e novas linhas
-SELECIONAR:(4 FORMAS)
    -1ª FORMA: Direto pelo nome das colunas
    -2ª FORMA: Pelos indices das colunas
    -3ª FORMA: Pelos indices das linhas e pelo nome das colunas
    -4ª FORMA: Pelos indices booleanos(True e False)
"""
#1ª FORMA


















