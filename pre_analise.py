# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 00:28:29 2023

@author: Diego
"""
#%%
from data_collection import bank_data, tickers, pd, np, plt, dt

#%% Acesse os dados usando bank_data['BAC'], bank_data['C'], etc.
bank_data['BAC']
# acessar a série de fechamentos 'closes' do BAC
bank_data['BAC']['close'].plot(figsize=(12, 4))
plt.xticks(rotation=30)
plt.tight_layout()

#%%
bank_data['C']
# acessar a série de fechamentos 'closes' do C - CitiGroup
bank_data['C']['close'].plot(figsize=(12, 4))
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

#%% Criar um parplot usando seaborn no dataframe de retorno
returns['BACReturn'].plot(figsize=(12, 4))

#%%
returns['GSReturn'].plot(figsize=(12, 4))

#%%
returns['CReturn'].plot(figsize=(12, 4))

#%%
returns['JPMReturn'].plot(figsize=(12, 4))

#%%
returns['MSReturn'].plot(figsize=(12, 4))

#%%
returns['WFCReturn'].plot(figsize=(12, 4))

'''
Nota-se que nos anos de 2008-2009 houve volatilidade excessiva dos retornos, 
O que era de se esperar devido a crise
Nos anos 2011-2012 também foi percebido uma volatilidade acentuado nos retornos
'''

#%% Criar um parplote do dataframe de retorno
import seaborn as sns
sns.pairplot(returns[1:]) 
# apartir de 1 pois a linha 0 contem valores NaN

'''
O pairplote gerado mostrar uma correlação entre os retornos de cada banco
Isso ocorre pois esses ativos fazem parte de um mesmo 'Índice' S&P 500
'''
#%%vamos descobrir o pior dia de returno de cada banco
returns.idxmin()
'''
 Alguns bancos teve seus piores retorno em 20/01/2009
 Essa data coincide com o dia da Posse do ex-presidente Obama
 Provavelmente alguns investidores entraram em pânico devido 
 a uma transição política tão relevante.
'''

#%% vamos descobrir o melhor dia de returno de cada banco
returns.idxmax()


#%% exemplo de como descobri o pior e o melhor retorno de determinado banco
returns['BACReturn'].min() #pior

returns['BACReturn'].max() #melhor

#%%
'''
 Descobrir qual ação é a mais arriscada durante todo o período de tempo.
 para isso devemos analisar os devios padroes das series de retorono 
e identificar qual ação é mais arriscada nos anos de 2006 a 2016.
'''
returns.std()

#Como CitiGroup(CReturn) é o que maior desvio, então ele é o mais volátio
#Cosequentimente o mais arriscado

#%% 
'''
VAMOS FILTRAR ESSES DADOS PARA 2015
Quremos agora descobrir a ação mais 
arriscado para o ano 2015
'''

#conveter o index(que são str) em 'TimeStamp'
returns.index = pd.to_datetime(returns.index)

type(returns.index)
returns.index[0]

#%% 
'''Agora devemos coverter os TimeStamps em objetos tipo 'date' 
e especificar para ele retornar somente datas a partir de (2015, 1, 1)
e anterior a (2016, 1, 1)
'''
returns[(returns.index.date >= dt.date(2015, 1, 1)) & (returns.index.date < dt.date(2016, 1, 1))].std()

'''
Agoran,com as datas filtradas para o ando de 2015, pode-se notar que
os Bancos que tiveram maior volatilidade de retornos foram o Morgan Stanley
e o Bank of America.
'''


#%% Gráfico distplot dos retornos de 2015 para o Morgan Stanley
sns.distplot(returns[(returns.index.date >= dt.date(2015, 1, 1)) & (returns.index.date < dt.date(2016, 1, 1))]['MSReturn'])

#%% Gráfico distplot dos retornos de 2008 para o CitiGroup
sns.distplot(returns[(returns.index.date >= dt.date(2008, 1, 1)) & (returns.index.date < dt.date(2009, 1, 1))]['CReturn'])


#%%
'''  MAIS VISUALIZAÇÕES   '''
sns.set_style('whitegrid')

# gráfico de linha mostrando o preço  de fechamento para cada banco para todo o índice de tempo
for tick in tickers:
    bank_stocks[tick]['close'].plot(figsize=(12, 4), label=tick)
plt.legend()

#%% 2º forma de plotar o gráfico de fechamentos
bank_stocks.xs(key='close', level='Stock Info', axis = 1).plot(figsize=(12, 4))
plt.legend()
