import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://rateyourmusic.com/genre/rock/")
time.sleep(25)

content = driver.page_source

soup = BeautifulSoup(content, 'html.parser')

# # URL da página da RateYourMusic sobre rock
# url = 'https://rateyourmusic.com/genre/rock/'
# resposta = requests.get(url)
# soup = BeautifulSoup(resposta.content, 'html.parser')

# Encontrar todos os elementos 'li' com a classe 'hierarchy_list_children'
todos_generos = soup.find_all('ul', class_='hierarchy_list')

print(todos_generos)

# Iterar sobre cada elemento encontrado e extrair o texto dentro da tag <a>
# print("Gêneros de rock:")
# for genero in todos_generos:
#     link = genero.find('a', href=True)
#     if link:
#         nome_genero = link.get_text()
#         print(nome_genero)
