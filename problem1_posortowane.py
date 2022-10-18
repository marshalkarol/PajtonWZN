import rich
from rich.progress import track
from collections import defaultdict
from ascii_graph import Pyasciigraph
from ascii_graph import colors
from ascii_graph.colordata import vcolor
import sys
import argparse
from ast import arg

parser = argparse.ArgumentParser()
parser.add_argument('-f','--file_name', default = 'live02/pan-tadeusz.txt', required = False)
parser.add_argument('-v', '--verse', default = 10, required = False)
parser.add_argument('-l', '--length', default = 0, required = False)

args = parser.parse_args()

#kolejność parametrów = nazwa, wiersz 
# & C:/Users/karol/.pyenv/pyenv-win/versions/3.9.13/python.exe "c:/Users/karol/Desktop/studia/2 stopień/semestr 3/python/live02/problem3_posortowane.py" -f live02/pan-tadeusz.txt -v 12 -l 2

# print(f'{args.file_name}')   #stringi
nazwa = args.file_name
wiersze = args.verse
length = args.length


with rich.progress.open(nazwa, 'r', encoding='utf8') as f:
    dictionary={}
    znaki=[',', '.', '!', '?', ';', ':', '*', '(', ')', '…', '-', '—', '+', '"', '^', '&', '[', '}', '{', '}']
    for line in f:
        line = line.strip().lower() #usuwanie spacji i mniejsze litery
        if len(line) == 0:
            continue
    
        for i in range(len(znaki)):
            line=line.replace(znaki[i], '') #usuwanie znakow zamieszczonych w liscie znaki


        line = line.split() #usuwanie niepotrzebnych spacji
        for word in line:
            if len(word) > int(length):
                dictionary[word] = dictionary.get(word, 0) + 1 #dodowanie wartosci dla kazdego slowa w slowniku

    sorted_dict= sorted(dictionary.items(), reverse = True, key = lambda t: t[1]) #sortowanie

    pattern = [colors.Red, colors.IRed, colors.Gre, colors.Blu, colors.Pur]
    data = vcolor(sorted_dict[0:int(wiersze)], pattern) #ustawianie powtarzających się kolorowych linii
    
    graph = Pyasciigraph() #rysowanie
    for line in graph.graph('sorted words', data):
        print(line)