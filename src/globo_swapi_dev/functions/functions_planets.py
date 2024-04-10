import pandas as pd


def find_hottest_planet(dados_json):

    df = pd.DataFrame(dados_json)

    def categorize_climate(climate):
        if 'árido' in climate:
            return 1
        else:
            return 0

    df['climate_category'] = df['climate'].apply(categorize_climate)

    sorted_df = df.sort_values(by=['climate_category', 'orbital_period', 'gravity'], ascending=[False, True, False])

    hottest_planet = sorted_df.iloc[0]

    return hottest_planet
