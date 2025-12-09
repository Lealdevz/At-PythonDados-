from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from models import Movie

def get_soup(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def extrair_catalogo(url, limite):
    soup = get_soup(url)
    ul_lista = soup.find('ul', class_='ipc-metadata-list')
    li_lista = ul_lista.find_all('li', class_='ipc-metadata-list-summary-item')
    catalog = []
    for item in li_lista[:limite]:
        try:
            titulo = item.find('h3', class_='ipc-title__text').get_text()
            ano = item.find('span', class_='cli-title-metadata-item').get_text()
            ano_int = int(ano)
            nota = item.find('span', class_='ipc-rating-star--rating').get_text()
            nota_float = float(nota.replace(',', '.'))

            filme = Movie(titulo, ano_int, nota_float)
            catalog.append(filme)
        except Exception as e:
            print(e)
            continue
    return catalog