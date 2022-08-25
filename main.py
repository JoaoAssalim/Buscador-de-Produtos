import requests
from bs4 import BeautifulSoup

prods = []
p = input('Digite o produto que deseja buscar: ').upper()

def flipkart():
    response = requests.get(f'https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2') #pega resposta da page
    HTML = response.content
    site = BeautifulSoup(HTML, 'html.parser') #pega html da pagina

    produtos = site.findAll('div', attrs={'_2kHMtA'}) #pega todos os itens com essa div

    for produto in produtos:
        titulo = produto.find('div', attrs={'class':'_4rR01T'})
        titulo = titulo.text
        preco = produto.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
        preco = preco.text

        if p in titulo.upper():
            prods.append([titulo, preco])
def mercadolivre():
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
                prods.append([titulo, preco])

flipkart()
mercadolivre()

for prod in prods:
    print(prod)
