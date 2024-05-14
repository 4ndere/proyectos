# Docs Tago para Python 
# https://api.docs.tago.io/#31985b63-9c44-429c-8281-737f7d91d8a5

import requests
import json

url = "https://api.tago.io/data/?qty=1"

payload={}
headers = {
  'device-token': 'ingresar token!!!'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Convertir la respuesta a JSON
data = json.loads(response.text)

# Imprimir el valor de "variable"
print(data['result'][0]['variable'])
