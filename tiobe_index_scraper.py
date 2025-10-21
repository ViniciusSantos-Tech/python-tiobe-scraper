#Feito por Vincius Santos-Tech
# Web Scraper para TIOBE Index - Rankings de Linguagens de Programação

import requests
from bs4 import BeautifulSoup

url = 'https://www.tiobe.com/tiobe-index/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tabela = soup.find('table', {'id': 'top20'})
if tabela:
    print("------------ TABELA ENCONTRADA!-------------")
    linhas = tabela.find_all('tr')

    for linha in linhas[1:]:
        colunas = linha.find_all('td')
        if len(colunas) >= 6: 
            posicao = colunas[0].text.strip()
            linguagem = colunas[4].text.strip()  
            rating = colunas[5].text.strip()     
            print(f"Posição {posicao}: {linguagem} - {rating}")
else:
    print("Tabela não encontrada")
