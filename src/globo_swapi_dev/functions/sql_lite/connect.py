import sqlite3

import pandas as pd
from src.globo_swapi_dev.functions.common_functions import silver_save
import logging

# Criação de um logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
logger = logging.getLogger('meu_logger')
logger.addHandler(console_handler)

def save(df1, table_name: str):

    silver_save(df1, table_name)

    df = pd.DataFrame(df1)

    conexao = sqlite3.connect(f"{table_name}.db")

    logging.info(f'Iniciando a gravação no banco de dados do endpoint {table_name}!')
    df.to_sql('dados_json', conexao, if_exists='replace', index=False)

    conexao.commit()
    conexao.close()
