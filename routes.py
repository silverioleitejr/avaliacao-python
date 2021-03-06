# Dependencia flask
# pip install flask
# pip install flask_sqlalchemy
# pip install mysql-connector-python
# pip install mysqlclient

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

#Bibliotecas
from flask import Flask, request

app = Flask("demo")
app.run()

