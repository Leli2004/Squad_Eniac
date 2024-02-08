######## Arquivo para usar com o Flask 

#importar flask:
from flask import Flask, render_template

import urllib.request, json

app = Flask(__name__)

@app.route("/") 
def hello():
   return '<h1>Olá, mundo!</h1>'
