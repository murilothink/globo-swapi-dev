import re

import requests


def get_api_films(endpoint):
    """
    Fetches data from the SWAPI endpoint.
    """

    url = f"https://swapi.dev/api/{endpoint}/"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data from {endpoint}. Status code: {response.status_code}")
        return None


def get_data_from_url(url):
    """
    Função para fazer uma solicitação GET para uma URL e retornar os dados JSON.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_name_from_url(url):
    try:
        if url != "None":
            response = requests.get(url)
            if response.status_code == 200 and re.match(r".*https://swapi.dev/api/films", url):
                return response.json().get('title', None)
            else:
                return response.json().get('name', None)
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
