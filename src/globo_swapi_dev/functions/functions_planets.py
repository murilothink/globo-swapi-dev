import pandas as pd


def find_hottest_planet(dados_json):
    # Converta o dicionário em um DataFrame
    df = pd.DataFrame(dados_json)

    # Defina uma função para categorizar o clima (árido = 1, não árido = 0)
    def categorize_climate(climate):
        if 'árido' in climate:
            return 1
        else:
            return 0

    # Adicione uma nova coluna 'climate_category' com base na função
    df['climate_category'] = df['climate'].apply(categorize_climate)

    # Ordene o DataFrame com base nos critérios
    sorted_df = df.sort_values(by=['climate_category', 'orbital_period', 'gravity'], ascending=[False, True, False])

    # Obtenha o planeta mais quente (primeira linha)
    hottest_planet = sorted_df.iloc[0]

    return hottest_planet
