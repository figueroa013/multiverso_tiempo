from .Nodo import Nodo
class Grafo:
    def __init__(self):
        self.nodos = {}

    def agregar_nodo(self, valor):
        if valor not in self.nodos:
            self.nodos[valor] = Nodo(valor)

    def eliminar_nodo(self, valor):
        if valor in self.nodos:
            # Eliminar el nodo de la lista de vecinos de otros nodos
            nodo_a_eliminar = self.nodos[valor]
            for vecino in nodo_a_eliminar.vecinos:
                vecino.eliminar_vecino(nodo_a_eliminar)
            # Eliminar el nodo del grafo
            del self.nodos[valor]

    def agregar_arista(self, valor1, valor2):
        if valor1 in self.nodos and valor2 in self.nodos:
            self.nodos[valor1].agregar_vecino(self.nodos[valor2])
            self.nodos[valor2].agregar_vecino(self.nodos[valor1])

    def eliminar_arista(self, valor1, valor2):
        if valor1 in self.nodos and valor2 in self.nodos:
            self.nodos[valor1].eliminar_vecino(self.nodos[valor2])
            self.nodos[valor2].eliminar_vecino(self.nodos[valor1])

    def buscar_nodo(self, valor):
        return self.nodos.get(valor, None)

    def mostrar_grafo(self):
        for nodo in self.nodos.values():
            print(f"{nodo}: {[vecino.valor for vecino in nodo.vecinos]}")

    def dfs(self, valor_inicial):
        visitados = set()
        resultado = []

        def _dfs(nodo):
            visitados.add(nodo)
            resultado.append(nodo.valor)
            for vecino in nodo.vecinos:
                if vecino not in visitados:
                    _dfs(vecino)

        nodo_inicial = self.nodos.get(valor_inicial, None)
        if nodo_inicial:
            _dfs(nodo_inicial)
        return resultado

    def bfs(self, valor_inicial):
        visitados = set()
        cola = []
        resultado = []

        nodo_inicial = self.nodos.get(valor_inicial, None)
        if nodo_inicial:
            cola.append(nodo_inicial)
            visitados.add(nodo_inicial)

            while cola:
                nodo = cola.pop(0)
                resultado.append(nodo.valor)
                for vecino in nodo.vecinos:
                    if vecino not in visitados:
                        cola.append(vecino)
                        visitados.add(vecino)

        return resultado

    def detectar_ciclo(self):
        visitados = set()

        def dfs(nodo, padre):
            visitados.add(nodo)
            for vecino in nodo.vecinos:
                if vecino not in visitados:
                    if dfs(vecino, nodo):
                        return True
                elif vecino != padre:
                    return True
            return False

        for nodo in self.nodos.values():
            if nodo not in visitados:
                if dfs(nodo, None):
                    return True
        return False
