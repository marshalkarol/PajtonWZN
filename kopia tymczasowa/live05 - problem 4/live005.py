import requests
from bs4 import BeautifulSoup
import json

req = requests.get('https://www.imdb.com/name/nm0001569/')

# print(req.status_code) 
# print(req.text)
# print(req.request.headers) #user agent - wysyła info, że jest pajtonem. Niektóre strony blokują scrape'owanie z pajtona

soup = BeautifulSoup(req.text, 'html.parser')

# filmo-category-section

films = soup.find('div', {'class': 'filmo-category-section'})

# print(films.text)

# filmo-row

chuck_films = []

for film in films.find_all('div', {'class': 'filmo-row'}):
    span = film.find('span')
    title = film.find('a')
    print(span.text.strip(), title.text.strip(), title['href'])
    chuck_films.append((span.text.strip(), title.text.strip(), title['href']))

print(chuck_films)

with open('live05 - problem 4/chuck_films.json', 'w') as f:
    json.dump(chuck_films, f, encoding = 'utf8')