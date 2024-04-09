import pandas as pd


def count_occurrences_names(dados_json):
    campos = [
        'characters_url24123121', 'characters_url24123122', 'characters_url24123123',
        'characters_url24123124', 'characters_url24123125', 'characters_url24123126',
        'characters_url24123127', 'characters_url24123128', 'characters_url24123129',
        'characters_url24123130', 'characters_url24123131', 'characters_url24123132',
        'characters_url24123133', 'characters_url24123134', 'characters_url24123135',
        'characters_url24123136', 'characters_url24123137', 'characters_url24123138',
        'characters_url24123139', 'characters_url24123140', 'characters_url24123141',
        'characters_url24123142', 'characters_url24123143', 'characters_url24123144',
        'characters_url24123145', 'characters_url24123146', 'characters_url24123147',
        'characters_url24123148', 'characters_url24123149', 'characters_url24123150',
        'characters_url24123151', 'characters_url24123152', 'characters_url24123153',
        'characters_url24123154', 'characters_url24123155', 'characters_url24123156',
        'characters_url24123157', 'characters_url24123158', 'characters_url24123159',
        'characters_url24123160'
    ]

    resultados = []

    for campo in campos:
        contagem = dados_json[campo].value_counts()
        resultados.append(contagem)

    resultados_df = pd.concat(resultados)

    total_ocorrencias = resultados_df.groupby(level=0).sum()

    nomes_repetidos = total_ocorrencias[total_ocorrencias > 1]

    return nomes_repetidos,
