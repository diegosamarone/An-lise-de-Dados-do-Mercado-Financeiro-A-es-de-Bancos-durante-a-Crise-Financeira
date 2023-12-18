# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 00:28:29 2023

@author: Diego
"""
#%%
from analise_mercado_financeiro import bank_data, tickers, pd, np, plt

#%% Acesse os dados usando bank_data['BAC'], bank_data['C'], etc.
bank_data['BAC']
# acessar a série de fechamentos 'closes' do BAC
bank_data['BAC']['close'].plot()
plt.xticks(rotation=30)
plt.tight_layout()

#%%
bank_data['C']
# acessar a série de fechamentos 'closes' do C - CitiGroup
bank_data['C']['close'].plot()
plt.xticks(rotation=30)
plt.tight_layout()

# o mesmo pode ser feito para os demais bancos

#%% concatenar os DataFrames do banco juntos em um único chamado bank_stocks
bank_stocks = pd.concat([bank_data['BAC'], bank_data['C'], bank_data['GS'], bank_data['JPM'], bank_data['MS'], bank_data['WFC']], axis=1, keys=tickers)


#%% Defina os níveis dos nomes das colunas
bank_stocks.columns.names = ['Bank Ticker','Stock Info']

#%%verificar o cabeçalho
bank_stocks.head()

#Agora as colunas possuem dois níveis: 
   #1º nvl - Tickers dos bancos
   #2º nvl - Clases de dados financeiros dos bancos

#%% ANÁLISE EXPLORATÓRIA

# Preço maximo de fechamento para o estoque de cada banco durante o periodo 
# Vamos usar o metodo .xs() para concatenar a coluna de 'close' fechamento de cada banco

bank_stocks.xs(key='close', axis=1, level='Stock Info').max()

#%% Agora vamos trabalhor com as series de retorno do ativos percentuais. 
# Cirar um dataframe os retornos para a ação de cada banco

returns = pd.DataFrame()

#%% Usar o método  pct_change() na cluna 'close' para criar uma coluna que represa o valor de retorno
# Através de um loop for criar uma coluna de retorno para cada banco

for tick in tickers:
    returns[tick + 'Return'] = bank_stocks[tick]['close'].pct_change()
returns.head()