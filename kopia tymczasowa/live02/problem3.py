from collections import defaultdict
from ascii_graph import Pyasciigraph

f= open('live02/pan-tadeusz.txt','r', encoding= 'utf8') #otworzenie pliku
dictionary={}
znaki=[',', '.', '!', '?', ';', ':', '*', '(', ')', '…', '-']
for line in f:
    line = line.strip().lower() #usuwanie spacji i mniejsze litery
    if len(line) == 0:
        continue
    
    for i in range(len(znaki)):
        line=line.replace(znaki[i], '') #usuwanie znakow zamieszczonych w liscie znaki


    line = line.split() #usuwanie niepotrzebnych spacji
    for word in line:
        dictionary[word] = dictionary.get(word, 0) + 1 #dodowanie wartosci dla kazdego slowa w slowniku
f.close() #zamkniecie pliku

sorted_dict= sorted(dictionary.items(), reverse = True, key = lambda t: t[1])

graph = Pyasciigraph()
for line in graph.graph('Words', sorted_dict[0:50]):
    print(line)


#f= open('live02/pan-tadeusz.txt', encoding= 'utf8') #otworzenie pliku (stara wersja)
    # for line in f:
    #     print(line) (wypisywanie PT)

# dictionary={}
# znaki=[',', '.', '!', '?', ';', ':', '*', '(', ')', '…', '-', '—']
# for line in f:
#     line = line.strip().lower() #usuwanie spacji i mniejsze litery
#     if len(line) == 0:
#         continue
    
#     for i in range(len(znaki)):
#         line=line.replace(znaki[i], '') #usuwanie znakow zamieszczonych w liscie znaki


#     line = line.split() #usuwanie niepotrzebnych spacji
#     for word in line:
#         dictionary[word] = dictionary.get(word, 0) + 1 #dodowanie wartosci dla kazdego slowa w slowniku
# f.close() #zamkniecie pliku

# sorted_dict= sorted(dictionary.items(), reverse = True, key = lambda t: t[1])

# graph = Pyasciigraph()
# for line in graph.graph('Words', sorted_dict[0:50]):
#     print(line)