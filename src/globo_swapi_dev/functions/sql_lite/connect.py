import logging
import os
import sqlite3

import pandas as pd

from src.globo_swapi_dev.functions.common_functions import silver_save

# Criação de um logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
logger = logging.getLogger('meu_logger')
logger.addHandler(console_handler)

def save(df1, table_name: str, layer: str):

    df = pd.DataFrame(df1)

    silver_save(df, table_name, layer)
    path = os.path.join(os.getcwd(), layer + '_files_db')
    os.makedirs(path, exist_ok=True)
    conexao = sqlite3.connect(os.path.join(os.getcwd(), layer + '_files_db', f"{table_name}.db"))




    logging.info(f'Iniciando a gravação no banco de dados do endpoint {table_name}!')
    df.to_sql(layer, conexao, if_exists='replace', index=False)

    conexao.commit()
    conexao.close()
