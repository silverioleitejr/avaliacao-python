
################################################################
# Projeto de Avaliação - Python - KPMG
#
# Analista responsavel: Silverio Leije Jr
# Data: 06/03/2021
# Consultoria: Pasqualini
################################################################
# I.	1 rota que retornará o valor médio de todos os carros baseados no fabricante (coluna car_make agrupada pela média dos valores da coluna car_value);
# II.	1 rota que retornará o valor médio de um fabricante de carro passado como parâmetro no request (Após o cálculo de I, pode-se filtrar apenas o valor requerido);
# III.	1 rota que que retornará o valor médio de todos os carros baseados nas cidades correspondentes (coluna city agrupada pela média dos valores da coluna car_value);
# IV.	1 rota que retornará o valor médio dos carros de uma cidade passada como parâmetro no request (Após o cálculo de III, pode-se filtrar apenas o valor requerido);
#################################################################


#definir variais globais 
import pandas as pd
pd.options.display.float_format = '${:,.2f}'.format
path = "https://raw.githubusercontent.com/silverioleitejr/avaliacao-python/main/data/dataset.csv"
vendas_df = pd.read_csv(path)

#Bibliotecas para API
from fastapi import FastAPI 
from pydantic import BaseModel
import pyspark
from pyspark.sql import SparkSession
import pandas as pd

app = FastAPI()

#verificar se um valor é nulo
def isNaN(num):
    return num != num

# Esta função retorna um DataFrameGroupBy por Marca
def agruparMediaMarca():
  grouped_df = vendas_df.groupby(['car_make'])
  mean_df = grouped_df.mean()
  mean_df.drop(['id'], inplace=True, axis=1)
  mean_df.drop(['car_year'], inplace=True, axis=1)
  return mean_df

# Esta funcao retorna a media conforme o parametro informado do fabricante - car_make
def calcularMedia( fabricante = ''):
  agrupamento_df = agruparMediaMarca()
  filtro_query = 'car_make == ' '"' + fabricante + '"'
  filtro_df = agrupamento_df.query( filtro_query )

  media = filtro_df['car_value']

  return media


# gerar dataframe agrupamento de valores por cidades 
def agruparMediaCidade():
  spark = SparkSession.builder.getOrCreate()

  # Ler o dataframe de vendas 
  spark_df = spark.createDataFrame(vendas_df)

  # incluir o spark df no cataloga Spark
  spark_df.createOrReplaceTempView('spark_df')
  agrupar_cidade_df = spark_df.groupBy("city").mean("car_value")
  agrupar_cidade_df.show()
  return agrupar_cidade_df

#rota raiz
@app.get('/')
def raiz():
      return {"Mensagem" : "API de avaliação - codigo fonte escrito em python"}

### uvicorn main:app --reload
### http://127.0.0.1:8000/
### http://127.0.0.1:8000/docs

# rota para retornar media por fabricante
# item I da avaliação
# http://127.0.0.1:8000/valor-medio-todos-fabricante
@app.get('/valor-medio-todos-fabricante')
def media_fabricante():
  return agruparMediaMarca()
  
# rota para retornar media para fabricante informado no parametro
# item II da avaliação
# http://127.0.0.1:8000/valor-medio-fabricante/A
@app.get('/valor-medio-fabricante/{fabricante}')
def media_fabricante(fabricante:str):
  media = calcularMedia(fabricante)
  return { "car_make" : media}

# rota para retornar media por cidade - city
# item III da avaliação
# http://127.0.0.1:8000/valor-medio-cidade
@app.get('/valor-medio-todas-cidade')
def media_todas_cidades():
  return agruparMediaCidade()




