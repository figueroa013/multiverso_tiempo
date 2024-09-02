class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.vecinos = []  # Lista de nodos conectados

    def agregar_vecino(self, nodo):
        if nodo not in self.vecinos:
            self.vecinos.append(nodo)

    def eliminar_vecino(self, nodo):
        if nodo in self.vecinos:
            self.vecinos.remove(nodo)

    def __str__(self):
        return str(self.valor)
