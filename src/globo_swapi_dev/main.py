import re
import json
import re
from usecase.authentication.get_swapi import get_api_films, get_data_from_url, get_name_from_url
import pandas as pd
from tabulate import tabulate
import os

def create_table(data):
    """
    Creates a Pandas DataFrame and formats it as a table.
    """
    # Cria um DataFrame com os dados fornecidos
    df = pd.DataFrame(data['results'])

    # Trata todas as colunas que contêm listas
    for column in df.columns:
        if isinstance(df[column].iloc[0], list):
            # Converte a lista em uma string separada por vírgulas
            df[column] = df[column].apply(lambda x: ', '.join(x))
            # Divide a string em várias colunas
            df = df.join(df[column].str.split(', ', expand=True).add_prefix(f'{column}_url'))
            # Remove a coluna original
            df.drop(columns=[column], inplace=True)

    # Formata o DataFrame como uma tabela usando tabulate
    table1 = tabulate(df, headers='keys', tablefmt='pretty', showindex=False)
    table_data = df.to_dict(orient='records')

    return table_data
def create_table1(data):
    """
    Creates a table using Pandas.
    """
    table_data = []
    for key, value in data.items():
        if isinstance(value, list):
            # Se o valor é uma lista, expandir em colunas separadas
            for i, item in enumerate(value):
                new_key = f"{key}_{i + 1}"
                table_data.append({new_key: item})
        else:
            table_data.append({key: value})

    # Transforma a lista de dicionários em DataFrame
    df = pd.DataFrame(table_data)

    # Formata o DataFrame como uma tabela
    table = tabulate(df, headers='keys', tablefmt='pretty', showindex=False)

    return table
# def create_planets_from_json(json_data):
#     planets = []
#     for planet_data in json_data["results"]:
#         planet = Planet(
#             name=planet_data["name"],
#             rotation_period=planet_data["rotation_period"],
#             orbital_period=planet_data["orbital_period"],
#             diameter=planet_data["diameter"],
#             climate=planet_data["climate"],
#             gravity=planet_data["gravity"],
#             terrain=planet_data["terrain"],
#             surface_water=planet_data["surface_water"],
#             population=planet_data["population"],
#             residents=planet_data["residents"],
#             films=planet_data["films"],
#             created=planet_data["created"],
#             edited=planet_data["edited"],
#             url=planet_data["url"]
#         )
#         planets.append(planet)
#     return planets


# def process_data(data):
#     """
#     Função para processar os dados e extrair informações relevantes.
#     """
#     table_data = []
#     for key, value in data.items():
#         if isinstance(value, list):
#             for item in value:
#                 if isinstance(item, str) and item.startswith("https://swapi.dev/api/"):
#                     sub_data = get_data_from_url(item)
#                     if sub_data:
#                         table_data.extend(process_data(sub_data))
#                 else:
#                     table_data.append([key, item])
#         elif isinstance(value, dict):
#             table_data.extend(process_data(value))
#         else:
#             table_data.append([key, value])
#     return table_data

# def process_planet_data(planet_data):
#     """
#     Função para processar os dados de um planeta, incluindo a busca de mais informações sobre residentes e filmes.
#     """
#     #['data']['graph_client_id']
#     # Extraindo campos básicos do planeta
#     teste = create_planets_from_json(planet_data)
#
#     # Buscando mais informações sobre os residentes
#     residents_info = []
#     for resident_url in planet_data['residents']:
#         resident_data = get_data_from_url(resident_url)
#         if resident_data:
#             residents_info.append(resident_data)
#
#     # Buscando mais informações sobre os filmes
#     films_info = []
#     for film_url in planet_data['films']:
#         film_data = get_data_from_url(film_url)
#         if film_data:
#             films_info.append(film_data)
#
#     # Retornando os dados processados
#     return teste
def save_table_to_json(table_data, filename):
    """
    Salva os dados da tabela em um arquivo JSON.
    """
    with open(filename, 'w') as json_file:
        json.dump(table_data, json_file, indent=4)

def read_table_from_txt(path):
    """
    Lê os dados tabulares de um arquivo de texto (.txt) e retorna um DataFrame.
    """
    return pd.read_json(path)

    #return tabulate(df, headers='keys', tablefmt='pretty', showindex=False)

# Diretório onde os dados tabulares estão salvos
bronze_dir = "bronze"

import re
from tabulate import tabulate

def expand_urls_to_names(df):
    """
    Expande as URLs da API em cada coluna e substitui pelos nomes correspondentes.
    """
    print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))
    for column in df.columns:
        if re.match(r".*url\d+$", column) or column.endswith('url'):
            match = re.search(r"\d+$", column)
            if match:
                number = int(match.group())
                new_number = number + 24123121
                new_column_name = column[:-len(str(number))] + str(new_number)
                df[new_column_name] = df[column].apply(lambda url: get_name_from_url(url))
                #df.drop(columns=[column], inplace=True) # Se quiser excluir a coluna de URL após expandir, descomente esta linha
    return tabulate(df, headers='keys', tablefmt='pretty', showindex=False)


def main():
    endpoints = [
        'people',
        'planets',
        'starships',
        'vehicles',
        'species'
        ]

    swapi_data = {}

    for endpoint in endpoints:
        data = get_api_films(endpoint)
        if data:
            swapi_data[endpoint] = data
            if data:
                swapi_data[endpoint] = data
                if data:
                    # Criar a tabela
                    table = create_table(data)
                    print(f"Data from {endpoint}:\n")
                    print(table)
                    print("\n")
                print(f"Fetched {len(data['results'])} items from {endpoint}")
            else:
                print(f"Failed to fetch {endpoint} data.")

            # Nome do arquivo a ser salvo
            filename = f"{endpoint}_table.json"

            # Cria o diretório do endpoint dentro do diretório "bronze"
            endpoint_dir = os.path.join("bronze", endpoint)
            os.makedirs(endpoint_dir, exist_ok=True)

            # Salva os dados em um arquivo de texto dentro do diretório do endpoint
            save_table_to_json(table, os.path.join(endpoint_dir, filename))

    df = read_table_from_txt("/home/murilohg/Documentos/globo/globo-swapi-dev/src/globo_swapi_dev/bronze/people/people_table.json")
    df1 = expand_urls_to_names(df)
    print(df1)

    df2 = read_table_from_txt("/home/murilohg/Documentos/globo/globo-swapi-dev/src/globo_swapi_dev/bronze/planets/planets_table.json")
    df3 = expand_urls_to_names(df2)
    print(df3)

    df5 = read_table_from_txt("/home/murilohg/Documentos/globo/globo-swapi-dev/src/globo_swapi_dev/bronze/species/species_table.json")
    df6 = expand_urls_to_names(df5)
    print(df6)

    df7 = read_table_from_txt("/home/murilohg/Documentos/globo/globo-swapi-dev/src/globo_swapi_dev/bronze/starships/starships_table.json")
    df8 = expand_urls_to_names(df7)
    print(df8)

    df9 = read_table_from_txt("/home/murilohg/Documentos/globo/globo-swapi-dev/src/globo_swapi_dev/bronze/vehicles/vehicles_table.json")
    df10 = expand_urls_to_names(df9)
    print(df10)


if __name__ == "__main__":
    main()


