from src.globo_swapi_dev.functions.common_functions import expand_urls_to_names, read_table_from_txt
from src.globo_swapi_dev.functions.common_functions import get_endpoint_and_save
from src.globo_swapi_dev.functions.sql_lite.connect import save
import os
from src.globo_swapi_dev.configs.config import (BRONZE, SILVER, GOLD, PLANETS_TABLE, PEOPLE_TABLE, SPECIES_TABLE, STARSHIPS_TABLE,
                                                VEHICLES_TABLE, FILMS_TABLE)
from src.globo_swapi_dev.functions.functions_films import count_occurrences_names
from src.globo_swapi_dev.functions.functions_planets import find_hottest_planet
from src.globo_swapi_dev.functions.functions_starships import find_max_values


def run_process_bronze():
    get_endpoint_and_save()


def run_process_silver():
    save(
        expand_urls_to_names(
            read_table_from_txt(os.path.join(os.getcwd(), BRONZE, PEOPLE_TABLE, "people_table.json"))),
        PEOPLE_TABLE, SILVER)

    save(
        expand_urls_to_names(
            read_table_from_txt(os.path.join(os.getcwd(), BRONZE, PLANETS_TABLE, "planets_table.json"))),
        PLANETS_TABLE, SILVER)

    save(
        expand_urls_to_names(
            read_table_from_txt(os.path.join(os.getcwd(), BRONZE, SPECIES_TABLE, "species_table.json"))),
        SPECIES_TABLE, SILVER)

    save(
        expand_urls_to_names(
            read_table_from_txt(os.path.join(os.getcwd(), BRONZE, STARSHIPS_TABLE, "starships_table.json"))),
        STARSHIPS_TABLE, SILVER)

    save(
        expand_urls_to_names(
            read_table_from_txt(os.path.join(os.getcwd(), BRONZE, VEHICLES_TABLE, "vehicles_table.json"))),
        VEHICLES_TABLE, SILVER)
    save(
        expand_urls_to_names(
            read_table_from_txt(os.path.join(os.getcwd(), BRONZE, FILMS_TABLE, "films_table.json"))),
         FILMS_TABLE, SILVER)


def run_process_gold():
    save(
        count_occurrences_names(
            read_table_from_txt(os.path.join(os.getcwd(), SILVER, FILMS_TABLE, "films_table.json"))), "films_gold",
        GOLD)

    save(
        find_hottest_planet(
            read_table_from_txt(os.path.join(os.getcwd(), SILVER, PLANETS_TABLE, "planets_table.json"))),
        PLANETS_TABLE, GOLD)

    save(
        find_max_values(
            read_table_from_txt(os.path.join(os.getcwd(), SILVER, STARSHIPS_TABLE, "starships_table.json"))),
        STARSHIPS_TABLE, GOLD)
