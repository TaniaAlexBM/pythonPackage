import requests

def unreleased():
    # *Realiza la petición a la API y recibe el json
    response = requests.get("https://codigofacilito.com/api/v2/workshops/unreleased")

    if response.status_code == 200:
        payload = response.json()
        return payload['data']