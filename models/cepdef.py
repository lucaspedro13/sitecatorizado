import requests
import json

cep = "69900812"

def limpar_cep(pesquisa):
    
    pesquisa = str(pesquisa)
    pesquisa = pesquisa.strip()

    if len(pesquisa) != 8:
        
        if len(pesquisa) >= 9:
            pesquisa = pesquisa.replace("-", "")
            pesquisa = pesquisa.replace(".", "")

        if len(pesquisa) <= 7:
            pesquisa = "cep inválido"
    
    return pesquisa

cep = limpar_cep(cep)
print(cep)