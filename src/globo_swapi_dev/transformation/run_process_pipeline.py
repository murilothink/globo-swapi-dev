from src.globo_swapi_dev.functions.common_functions import expand_urls_to_names, read_table_from_txt
from src.globo_swapi_dev.functions.common_functions import get_endpoint_and_save
from src.globo_swapi_dev.functions.sql_lite.connect import save
import os
from src.globo_swapi_dev.configs.config import (BRONZE, PLANETS_TABLE, PEOPLE_TABLE, SPECIES_TABLE, STARSHIPS_TABLE,
                                                VEHICLES_TABLE, FILMS_TABLE)


def run_process_bronze():
    get_endpoint_and_save()


def run_process_silver():
    save(expand_urls_to_names(read_table_from_txt(os.path.join(os.getcwd(), BRONZE, PEOPLE_TABLE, "people_table.json"))),
         PEOPLE_TABLE)
    save(expand_urls_to_names(read_table_from_txt(os.path.join(os.getcwd(), BRONZE, PLANETS_TABLE, "planets_table.json"))),
        PLANETS_TABLE)
    save(expand_urls_to_names(read_table_from_txt(os.path.join(os.getcwd(), BRONZE, SPECIES_TABLE, "species_table.json"))),
        SPECIES_TABLE)
    save(expand_urls_to_names(read_table_from_txt(os.path.join(os.getcwd(), BRONZE, STARSHIPS_TABLE, "starships_table.json"))),
         STARSHIPS_TABLE)
    save(expand_urls_to_names(read_table_from_txt(os.path.join(os.getcwd(), BRONZE, VEHICLES_TABLE, "vehicles_table.json"))),
         VEHICLES_TABLE)
    save(expand_urls_to_names(read_table_from_txt(os.path.join(os.getcwd(), BRONZE, FILMS_TABLE, "films_table.json"))),
         "films")
