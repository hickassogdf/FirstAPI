import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)
#Building api 
@app.route('/')
def homepage():
  return 'Essa é a API'

#Endpoint 1
@app.route('/pegarvendas')
def pegarvendas():
  tabela = pd.read_csv('12-18 - Criando API no Python.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total_vendas': total_vendas}
  return jsonify(resposta)


#rodar api
app.run(host='0.0.0.0')


