import pandas as pd


def find_max_values(df):

    max_mglt = df.loc[df['MGLT'].idxmax()][['name', 'MGLT', 'max_atmosphering_speed']]

    df['max_atmosphering_speed'] = pd.to_numeric(df['max_atmosphering_speed'], errors='coerce')

    if not df['max_atmosphering_speed'].isnull().all():

        df_without_nan = df.dropna(subset=['max_atmosphering_speed'])
        max_atmospheric_speed = df_without_nan.loc[df_without_nan['max_atmosphering_speed'].idxmax()][
            ['name', 'MGLT', 'max_atmosphering_speed']]
    else:
        max_atmospheric_speed = None

    result_union = pd.concat([max_mglt, max_atmospheric_speed], axis=1).T

    return result_union
