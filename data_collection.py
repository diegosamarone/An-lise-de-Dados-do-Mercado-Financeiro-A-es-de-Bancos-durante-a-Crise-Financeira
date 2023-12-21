# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 00:23:48 2023

@author: Diego
"""
#%%
import pandas_datareader as pdr
import pandas as pd
import numpy as np
import seaborn as sns
import datetime as dt
from matplotlib import pyplot as plt
#%%

api_key = 'SUA_CHAVE_API_ALPHA_VANTAGE'

start_date = dt.datetime(2006, 1, 1)

end_date = dt.datetime(2016, 1, 1)

# Lista de símbolos de ações dos bancos em ordem alfabética

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']


#%%
# iremos precisar de um dicionário para armazenar os DataFrames de cada banco
bank_data = {}


#%%
# Loop com um bloco 'try' para obter dados para cada banco
for bank in tickers:
    try:
        # Obtenha dados do Alpha Vantage
        data = pdr.av.time_series.AVTimeSeriesReader(
            symbols=bank,
            start=start_date,
            end=end_date,
            api_key=api_key
        ).read()

        # Armazene os dados no dicionário
        bank_data[bank] = data

        print(f"Dados do banco {bank} obtidos com sucesso")
    except Exception as e:
        print(f"Erro ao obter os dados do banco {bank}: {e}")

# bank_data agora contém DataFrames para cada banco

#%%
