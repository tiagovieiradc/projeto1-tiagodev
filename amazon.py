# importando bibliotecas
import time  # acesso ao horário e conversões
import requests  # solicitações HTTP
import pandas as pd  # manipular os dados e dataframe
# cria uma árvore de análise para as páginas analisadas
from bs4 import BeautifulSoup
import selenium  # automatiza a busca no site
from selenium import webdriver
# para criar scripts de testes automatizados
from selenium.common.exceptions import NoSuchElementException
# módulo options para  definir recursos para o Navegador
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json


# url de busca
url = 'https://www.amazon.com.br/s?k=fic%C3%A7%C3%A3o&i=stripbooks&s=most_sell&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=1X91OL2CGG1W6&qid=1634089436&sprefix=fic%2Cstripbooks%2C249&ref=sr_st_date-desc-rank'

# chamar o navegador
option = Options()
option.headless = False
# controlando o navegador --implementando com a solução ChromeDriverManager().install()
navegador = webdriver.Chrome(ChromeDriverManager().install())
navegador.get(url)

# pegando o grid de produtos da busca --usar full x path
div_grid = navegador.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]")
print(div_grid)
# navegador.quit()
html_content = div_grid.get_attribute('outerHTML')
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify())
# src__Wrapper-sc-1k0ejj6-3 eflURh
lista_de_produtos = soup.find_all(
    'div', class_='s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16')
for produto in lista_de_produtos:
    print('---------------------------------------------------------------------------')
    nome_produto = produto.select('div span')
    print('Nome do produto--> ' + produto.find('span',
          class_='a-size-medium a-color-base a-text-normal').get_text())
    preco_a_vista = produto.select('div span')
    print('Preço anterior--> ' + produto.find('span',
          class_='a-price a-text-price').get_text())
    preco_a_prazo = produto.select('div span')
    print('Preço à vista --> ' + produto.find('span',
          class_='a-price').get_text())
