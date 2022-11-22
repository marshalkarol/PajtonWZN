import time
import random

def timer(func):
    def timed(*args, **kwargs):
        times = []
        rand = random.randint(1,10)
        for i in range(rand):
            start = time.time()
            wynik = func(*args, **kwargs)
            stop = time.time()
            times.append(stop-start)
        mean = sum(times) / len(times)
        print(f"Sredni czas funkcji to: {mean} s")

        return wynik
    return timed

@timer
def funkc(n):
    suma = 0
    for i in range(0, 1000 * n):
        suma = suma + i
    return suma

n = random.randint(10000, 100000)
print(n)
funkc( n )