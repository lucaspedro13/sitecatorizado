
from flask import Flask, render_template, redirect, url_for, request , Blueprint
import requests
from models.pesqcep import cepdigitado
import json
#################################################












# parte do flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/localizacao")
def contatos():
    return render_template("localizacao.html")

@app.route("/horarios")
def horarios():
    return render_template("horarios.html")

@app.route("/endereco")
def endereco():
    return render_template("endereco.html")

@app.route("/pesquisacep", methods = ['GET', 'POST'])
def pesquisarcep():

    return render_template("pesquisacep.html")

@app.route("/pesquisacep/<pesquisacep>")
def limpar_cep(pesquisacep):
    
    pesquisacep = str(pesquisacep)
    pesquisacep = pesquisacep.strip()

    if len(pesquisacep) != 8:
        
        if len(pesquisacep) >= 9:
            pesquisacep = pesquisacep.replace("-", "")
            pesquisacep = pesquisacep.replace(".", "")

        if len(pesquisacep) <= 7:
            pesquisacep = "cep inválido"
        
        if len(pesquisacep) == 8:

            pesquisacep = requests.get(f'https://viacep.com.br/ws/{pesquisacep}/json')

            pesquisacep = pesquisacep.json()
    else:
       pesquisacep = requests.get(f'https://viacep.com.br/ws/{pesquisacep}/json')
       
       pesquisacep = pesquisacep.json() 

    return render_template("pesquisacep.html", pesquisacep=pesquisacep)


if __name__ == "__main__":
    app.run(debug=True)
