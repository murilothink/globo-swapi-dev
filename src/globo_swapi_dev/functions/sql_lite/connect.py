import sqlite3

import pandas as pd
from src.globo_swapi_dev.functions.common_functions import silver_save

def save(df1, table_name: str):

    silver_save(df1, table_name)

    df = pd.DataFrame(df1)

    conexao = sqlite3.connect(f"{table_name}.db")

    df.to_sql('dados_json', conexao, if_exists='replace', index=False)

    conexao.commit()
    conexao.close()
