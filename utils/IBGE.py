import json

import requests


def buscar_dados():
    res = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/26/municipios')
    todo = json.loads(res.text)

    for i in range(0,185):
        print(f"('{todo[i]['id']}','{todo[i]['nome']}'),")

buscar_dados()