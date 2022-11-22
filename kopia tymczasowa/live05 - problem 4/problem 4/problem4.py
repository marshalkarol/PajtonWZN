import argparse
from ast import arg
import requests
from bs4 import BeautifulSoup
import json

parser = argparse.ArgumentParser()
parser.add_argument('-f','--file_name', default = 'live05 - problem 4/problem 4/keanu_films.json', required = False)
args = parser.parse_args()
nazwa = args.file_name

req = requests.get('https://www.imdb.com/name/nm0000206/')
soup = BeautifulSoup(req.text, 'html.parser')

films = soup.find('div', {'class': 'filmo-category-section'})
keanu_films = []

for film in films.find_all('div', {'class': 'filmo-row'}):
    span = film.find('span')
    title = film.find('a')
    print(span.text.strip(), title.text.strip())
    keanu_films.append((span.text.strip(), title.text.strip()))

with open(nazwa, 'w') as f:
    json.dump(keanu_films, f)