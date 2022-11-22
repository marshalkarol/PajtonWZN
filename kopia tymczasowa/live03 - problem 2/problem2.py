import numpy as np
import argparse
import os
import matplotlib.pyplot as plt
from ising import Simulation
import time

t1 = time.time()

parser = argparse.ArgumentParser(description="Symulacja Isinga")
parser.add_argument("N", help="Wymiar siatki", type=int)
parser.add_argument("J", help="Integral", type=float)
parser.add_argument("beta", help="Beta", type=float)
parser.add_argument("B", help="Wartosc pola magnetycznego", type=float)
parser.add_argument("steps", help="Liczba kroków", type=int)
parser.add_argument("-d", help="Gestosc \"up\" spinow", type=float, default=0.5, choices=np.around(np.arange(0, 1.01, 0.01), 2), metavar="[0.00-1.00]")
parser.add_argument("-f", help="Nazwy plikow png", type=str, default="Step")
args = parser.parse_args()

for root, dirs, files in os.walk('./output'):
    for f in files:
        os.unlink(os.path.join(root, f))

S = Simulation(args.N, args.J, args.beta, args.B, args.steps, np.around(args.d, 2), args.f)

for s in S:
    s.make_image()

t2 = time.time()

print(t2-t1)

plt.plot(range(args.steps + 1), S.m)
plt.ylabel("Magnetyzacja")
plt.ylim((-1.1, 1.1))
plt.xlabel("Krok")
plt.title("Magnetyzacja jako funkcja kroków")
plt.grid()
plt.show()