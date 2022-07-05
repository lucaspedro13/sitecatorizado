from urllib import response
import requests
import json

print("qual seu cep?\n")

cep_client = input(str())

cep_client = cep_client.strip()

if len(cep_client) >= 9 :
    cep_client = cep_client.replace("-", "")
    cep_client = cep_client.replace(".", "")

r = requests.get(f'https://viacep.com.br/ws/{cep_client}/json/')

r = r.json()

print(r)
