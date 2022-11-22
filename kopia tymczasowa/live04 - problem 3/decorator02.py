class Ising:
    def __init__(self, hamiltonian = None):
        self._hamiltonian = hamiltonian
    
    def hamiltonian(self, func):
        self._hamiltonian = func
        return func

ising = Ising()

@ising.hamiltonian
def hamiltonian():
    return 0

print(ising._hamiltonian)