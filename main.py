import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

p = input('Digite nome do produto ou marca que deseja buscar: ').upper()

def flipkart():
    prods1 = []
    response = requests.get(f'https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2') #pega resposta da page
    HTML = response.content
    site = BeautifulSoup(HTML, 'html.parser') #pega html da pagina

    produtos = site.findAll('div', attrs={'_2kHMtA'}) #pega todos os itens com essa div

    for produto in produtos:
        titulo = produto.find('div', attrs={'class':'_4rR01T'})
        titulo = titulo.text
        preco = produto.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
        preco = preco.text[1:]
        preco = preco.replace(',', '.')

        preco = 'R$' + str(round(float(preco) / 15.63, 3))

        if p in titulo.upper():
            prods1.append([titulo, preco])
    return prods1
def mercadolivre():
    prods2 = []
    def buscar_page():
        response = requests.get(f'https://www.mercadolivre.com.br/ofertas?container_id=MLB779362-1&page=1')
        HTML = response.content
        site = BeautifulSoup(HTML, 'html.parser')

        pages = site.find('div', attrs={'class':'content content__margin'})
        proximo = site.findAll('a', attrs={'class':'andes-pagination__link'})
        proximo = proximo[-2]

        return proximo.text

    for i in range(1, int(buscar_page())+1):

        response = requests.get(f'https://www.mercadolivre.com.br/ofertas?container_id=MLB779362-1&page={i}')
        HTML = response.content
        site = BeautifulSoup(HTML, 'html.parser')

        produtos = site.findAll('div', attrs={'promotion-item__description'})

        for produto in produtos:
            titulo = produto.find('p', attrs={'class':'promotion-item__title'})
            titulo = titulo.text
            preco = produto.find('span', attrs={'class': 'promotion-item__price'})
            preco = preco.text

            if not '.' in preco:
                if len(preco) >= 7 and len(preco) < 8:
                    preco = f'R${preco[2:5]},{preco[5:7]}'
                elif len(preco) >= 8 and len(preco) < 9:
                    preco = f'R${preco[2:6]},{preco[6:8]}'
                
            if p in titulo.upper():
                prods2.append([titulo, preco])
    return prods2
def magazineluiza():
    prods3 = []
    response = requests.get(f'https://www.magazineluiza.com.br/selecao/ofertasdodia/') #pega resposta da page
    HTML = response.content
    site = BeautifulSoup(HTML, 'html.parser') #pega html da pagina
    produtos = site.findAll('li', attrs={'sc-gpcHMt bjNmTl'}) #pega todos os itens com essa div

    for produto in produtos:
        titulo = produto.find('h2', attrs={'class':'sc-fezjOJ gRRUnD'})
        titulo = titulo.text
        preco = produto.find('p', attrs={'class':'sc-kDTinF zuoFI sc-dcgwPl bvdLco'})
        preco = preco.text

        prods3.append([titulo, preco])
    return prods3

if len(flipkart()) > 0:
    print('Produtos na FlipKart:')
    for i in flipkart():
        print(i)
    df = pd.DataFrame(flipkart(), columns=['Produto', 'Preço'])
    table = df.to_dict('records')

    with open('produtosFlipKart.json', 'w', encoding='utf-8') as jp:
        js = json.dumps(table, indent=4)
        jp.write(js)
else:
    print('Produto ou Marca não Encontrada na FlipKart')

if len(mercadolivre()) > 0:
    print('Produtos no Mercado Livre:')
    for i in mercadolivre():
        print(i)
    df = pd.DataFrame(mercadolivre(), columns=['Produto', 'Preço'])
    table = df.to_dict('records')

    with open('produtosMercadoLivre.json', 'w', encoding='utf-8') as jp:
        js = json.dumps(table, indent=4)
        jp.write(js)
else:
    print('Produto ou Marca não Encontrada no Mercado Livre')

if len(magazineluiza()) > 0:
    print('Produtos no Magazine Luiza:')
    for i in magazineluiza():
        print(i)
    df = pd.DataFrame(magazineluiza()(), columns=['Produto', 'Preço'])
    table = df.to_dict('records')

    with open('produtosMagazineLuiza.json', 'w', encoding='utf-8') as jp:
        js = json.dumps(table, indent=4)
        jp.write(js) 
else:
    print('Produto ou Marca não Encontrada no Magazine Luiza')
