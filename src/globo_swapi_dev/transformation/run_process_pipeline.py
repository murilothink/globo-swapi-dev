from src.globo_swapi_dev.functions.common_functions import expand_urls_to_names, read_table_from_txt
from src.globo_swapi_dev.functions.common_functions import get_endpoint_and_save
from src.globo_swapi_dev.functions.sql_lite.connect import save


def run_process_bronze():
    get_endpoint_and_save()

def run_process_silver():
    save(expand_urls_to_names(read_table_from_txt(
        "/home/murilohg/Documentos/globo/globo-swapi-dev/src/globo_swapi_dev/bronze/people/people_table.json")), "people")
    save(expand_urls_to_names(read_table_from_txt(
        "/home/murilohg/Documentos/globo/globo-swapi-dev/src/globo_swapi_dev/bronze/planets/planets_table.json")), "planets")
    save(expand_urls_to_names(read_table_from_txt(
        "/home/murilohg/Documentos/globo/globo-swapi-dev/src/globo_swapi_dev/bronze/species/species_table.json")), "species")
    save(expand_urls_to_names(read_table_from_txt(
        "/home/murilohg/Documentos/globo/globo-swapi-dev/src/globo_swapi_dev/bronze/starships/starships_table.json")), "starships")
    save(expand_urls_to_names(read_table_from_txt(
        "/home/murilohg/Documentos/globo/globo-swapi-dev/src/globo_swapi_dev/bronze/vehicles/vehicles_table.json")), "vehicles")
    save(expand_urls_to_names(read_table_from_txt(
        "/home/murilohg/Documentos/globo/globo-swapi-dev/src/globo_swapi_dev/bronze/films/films_table.json")), "films")
