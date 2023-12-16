<h1>Análise de Dados do Mercado Financeiro: Ações de Bancos durante a Crise Financeira</h1>

 <div>
   
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
<img src="https://pandas-datareader.readthedocs.io/en/latest/_static/pandas-datareader-plain.svg" alt="datareader" width="100" height="30">

 </div>
 <div>
   
<h2>Relatório do Projeto:</h2>

<h3>Objetivo do Projeto</h3>

**Este projeto de dados tem como objetivo realizar uma análise exploratória dos preços das ações, concentrando-se especialmente nas ações de bancos. É importante destacar que este projeto é voltado para a prática de habilidades em visualização e manipulação de dados com bibliotecas específicas, não sendo uma análise financeira robusta.**

</div>

**Fonte de Dados**
* Utilizamos a **Alpha Vantage** como fonte de dados, que disponibiliza uma API gratuita para obtenção de dados financeiros incluindo informações sobre ações.

**Obtendo Dados**
* Para obter dados, é necessário uma chave de API gratuita fornecida pelo Alpha Vantage. As etapas incluem:
   - Obter uma chave de API no site do [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
   - Utilizar a chave de API no código fornecido.

**Coleta de Dados**
* Obtivemos dados sobre as ações de alguns bancos, como Bank of America, CitiGroup, Goldman Sachs, JPMorgan Chase, Morgan Stanley e Wells Fargo. Os dados foram coletados no período de 1 de janeiro de 2006 a 1 de janeiro de 2016 (o período pode, eventualmente, ser alterado para datas mais atuais).

**Informações Financeiras**
* Demonstramos como acessar informações financeiras sobre os bancos, como a série de fechamentos ('closes') do Bank of America.

**Concatenação de DataFrames**
* Utilizamos a função pd.concat para concatenar os DataFrames dos bancos em um único DataFrame chamado bank_stocks. Isso porque queremos que o DataFrame bank_stocks reuna informações consolidadas de todos os bancos. Os níveis dos nomes das colunas foram definidos para facilitar a análise.

**Próximos Passos**
* O projeto está em andamento, e os próximos passos incluirão análises mais aprofundadas, visualizações gráficas e possíveis modelagens preditivas, conforme necessário.

<div>
<br>
<h4>Tecnologias:</h4>
Python
<br>Jupyter Notebook
<br>Pandas
<br>Pandas-datareader
<br>Alpha Vantage API
<br>Numpy
<br>Matplotlib
</div>
