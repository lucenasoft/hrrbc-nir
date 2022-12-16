import requests

res = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/{pe}/mesorregioes').text

print(res.format())