# Web Scraping Sites com BeautifulSoup

Este projeto é somente para fins educacionais.

O código mostra como fazer web scraping de páginas de conteúdo dinâmico buscando produtos em especifico e retornando suas especificações e preços e salvando-as em um arquivo json.

Usei como base de busca os sites, Mercado Livre, FlipKart e Magazine luiza para extrair informações dos produtos e gerar um json com essas informações.  
**Important: Somente para fins educacionais**

## Prerequisites

O que você precisa para instalar o software e como instalá-los:

* Python 3.x
* ChromeDriver
* Chrome
* Some Python libraries following

### Instale as seguintes bibliotecas do python:

 * **requests** - Requests é a única biblioteca HTTP não OGM para Python, segura para consumo humano;
 * **pandas** - Biblioteca para auxiliar no manuseio dos dados;
 * **beautfulsoup4** - Biblioteca para retirar dados do HTML do arquivo;
 * **json** - Biblioteca para criar os arquivos json com preço e nome dos produtos.

Rode:
```
pip install -r requirements.txt
choco install chromedriver
```

## Rodando o codigo

```
python main.py
```
