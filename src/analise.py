import pandas as pd

def classificar_filmes(nota):
    if nota >= 9.0:
        return "Obra-prima"
    elif nota >= 8.0:
        return "Excelente"
    elif nota >= 7.0:
        return "Bom"
    else:
        return "Mediano"

def gerar_relatorio(engine):
    df_movies = pd.read_sql_table('movies', engine)
    df_series = pd.read_sql_table('series', engine)

    df_movies['categorias'] = df_movies['rating'].apply(classificar_filmes)
    tabela_resumo = pd.crosstab(df_movies['year'], df_movies['categorias'])

    selecao = df_movies[['title', 'rating', 'categorias']]

    df_organizado = df_movies.sort_values(by='rating', ascending=False)
    df_filtrado = df_organizado[df_organizado['rating'] >= 9.0]

    try:
        df_movies.to_csv('movies.csv', index=False, encoding='utf-8')
        df_series.to_csv('series.csv', index=False, encoding='utf-8')

        df_movies.to_json('movies.json', orient='records', indent=4, force_ascii=False)
        df_series.to_json('series.json', orient='records', indent=4, force_ascii=False)
    except Exception as e:
        print(e)

    return tabela_resumo, selecao, df_filtrado