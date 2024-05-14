import requests

def obtener_valor():
    base_url = "https://api.thethings.io/v2/things/"
    recursos = ["caudal", "nivel", "volumenAcum"] # Acá agregar variables para consultar

    while True:
        key = input("Por favor, introduce la clave (o 'salir' para terminar): ")
        if key.lower() == 'salir':
            break

        for recurso in recursos:
            url = base_url + key + "/resources/" + recurso

            # Realizar la solicitud GET al URL
            response = requests.get(url)

            # Comprobar si la solicitud fue exitosa
            if response.status_code == 200:
                data = response.json()  # Convertir la respuesta a JSON
                print(f"El valor de '{recurso}' es: {data}")
            else:
                print(f"Hubo un error al realizar la solicitud: {response.status_code}")

if __name__ == "__main__":
    obtener_valor()
