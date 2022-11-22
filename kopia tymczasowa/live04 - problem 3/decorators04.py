class Ising:
    def __init__(self, hamiltonian = None):
        self.hamiltonian = hamiltonian

ising = Ising()
ising._hamiltonian = 'My Hamiltonian'

print(ising.hamiltonian)


#trochę mi się teraz nie chce już pisać, przekopiuję później xd