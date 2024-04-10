import json
import logging
import os
import re

import pandas as pd
from tabulate import tabulate

from src.globo_swapi_dev.functions.get_swapi import get_name_from_url, get_api_films

# Criação de um logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
logger = logging.getLogger('meu_logger')
logger.addHandler(console_handler)


def create_table(data):
    df = pd.DataFrame(data['results'])
    logging.info('Iniciando o tratamento de colunas com que contêm listas')
    for column in df.columns:
        if isinstance(df[column].iloc[0], list):
            df[column] = df[column].apply(lambda x: ', '.join(x))

            df = df.join(df[column].str.split(', ', expand=True).add_prefix(f'{column}_url'))

            df.drop(columns=[column], inplace=True)

    table_data = df.to_dict(orient='records')
    logging.info('Fim do tratamento!')
    return table_data


def read_table_from_txt(path):
    return pd.read_json(path)


def expand_urls_to_names(df):
    logging.info(
        'Iniciando o tratamento que Expande as URLs da API em cada coluna e substitui pelos nomes correspondentes')
    # print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))
    for column in df.columns:
        if re.match(r".*url\d+$", column) or column.endswith('url') or column.endswith('world'):
            match = re.search(r"\d+$", column)
            if match:
                number = int(match.group())
                new_number = number + 24123121
                new_column_name = column[:-len(str(number))] + str(new_number)
                df[new_column_name] = df[column].apply(lambda url: get_name_from_url(url))
                df.drop(columns=[column], inplace=True)
            else:
                new_column_name = column + "_modified"
                df[new_column_name] = df[column].apply(lambda url: get_name_from_url(url))
                df.drop(columns=[column], inplace=True)
    logging.info('Fim do tratamento!')
    return df
    # tabulate(df, headers='keys', tablefmt='pretty', showindex=False))


def silver_save(df, endpoint):
    logging.info(f'Iniciando Gravação Silver table {endpoint}!')
    endpoint_dir = os.path.join("silver", endpoint)
    os.makedirs(endpoint_dir, exist_ok=True)
    df.to_json(os.path.join(endpoint_dir, f"{endpoint}_table.json"), orient='records')
    logging.info(f'Fim Gravação Silver table {endpoint}!')


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

    df = pd.DataFrame(table_data)

    table = tabulate(df, headers='keys', tablefmt='pretty', showindex=False)

    return table


def save_table_to_json(table_data, filename):
    print(tabulate(table_data, headers='keys', tablefmt='pretty', showindex=False))
    with open(filename, 'w') as json_file:
        json.dump(table_data, json_file, indent=4)


def get_endpoint_and_save():
    endpoints = [
        'people',
        'planets',
        'starships',
        'vehicles',
        'species',
        'films',
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


def expand_urls_to_names(df):
    logging.info("Expande as URLs da API em cada coluna e substitui pelos nomes correspondentes.")

    for column in df.columns:
        if re.match(r".*url\d+$", column) or column.endswith('url') or column.endswith('world'):
            match = re.search(r"\d+$", column)
            if match:
                number = int(match.group())
                new_number = number + 24123121
                new_column_name = column[:-len(str(number))] + str(new_number)
                df[new_column_name] = df[column].apply(lambda url: get_name_from_url(url))
                df.drop(columns=[column], inplace=True)
            else:
                new_column_name = column + "_modified"
                df[new_column_name] = df[column].apply(lambda url: get_name_from_url(url))
                df.drop(columns=[column], inplace=True)

    return df


def read_table_from_txt(path):
    logging.info(f'Iniciando a leitura do pat {path}!')
    return pd.read_json(path)


def silver_save(df, endpoint, layer):
    logging.info(f'Iniciando a gravação na silver do endpoint {endpoint}!')
    print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))
    endpoint_dir = os.path.join(layer, endpoint)
    os.makedirs(endpoint_dir, exist_ok=True)
    df.to_json(os.path.join(endpoint_dir, f"{endpoint}_table.json"), orient='records')
