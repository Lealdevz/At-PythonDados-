import json
from models import Series
import scrap
import database
import analise

def main():
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    catalog = scrap.extrair_catalogo(config['imbd_url'], config['n_filmes'])

    serie1 = Series("Supernatural", 2005, 15, 327)
    serie2 = Series("Dexter", 2006, 8, 96)
    catalog.append(serie1)
    catalog.append(serie2)

    engine = database.salvar_banco(catalog, config['db_nome'])
    tabela_resumo, selecao, df_filtrado = analise.gerar_relatorio(engine)

    print("exibindo os 10 primeiros filmes") ## questão 1 e 2 e 5
    for filme in catalog[:10]:
        print(filme)
    
    print("exibindo os filmes com nota maior ou igual a 9.0") ## questão 8
    print(df_filtrado)
    
    print("exibindo os filmes com categoria") ## questão 9
    print(selecao)
    
    print("exibindo o resumo de notas por categoria") ## questão 10
    print(tabela_resumo)

if __name__ == "__main__":
    main()
