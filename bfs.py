import os
from collections import deque

os.system("cls")


class BreadthFirstAlgorithm:
    def __init__(self, grafo, inicio, objetivo=None):
        self.grafo = grafo
        self.inicio = inicio
        self.objetivo = objetivo

    def breadthFirstSearch(self, fila, visitados, caminho, objetivo):
        while fila:
            vertice = fila.pop(0)
            caminho.append(vertice)
            visitados.add(vertice)

            if vertice == objetivo:
                return caminho

            for vizinho in self.grafo[vertice]:
                if vizinho not in visitados:
                    fila.append(vizinho)
                    visitados.add(vizinho)

        return caminho

    def search(self):
        fila = [self.inicio]
        visitados = set()
        caminho = []
        return self.breadthFirstSearch(fila, visitados, caminho, self.objetivo)


if __name__ == "__main__":
    grafo = {
        "A": ["B", "C", "D"],
        "B": ["E", "F"],
        "C": ["G"],
        "D": ["H", "I"],
        "E": ["J"],
        "F": [],
        "G": ["K"],
        "H": ["L"],
        "I": ["M", "N"],
        "J": [],
        "K": [],
        "L": [],
        "M": [],
        "N": ["O", "P"],
        "O": [],
        "P": ["Q"],
        "Q": [],
    }

    inicio = "A"
    objetivo = "Q"

    bfs = BreadthFirstAlgorithm(grafo, inicio, objetivo)
    resultado = bfs.search()

    if objetivo:
        print(f"Caminho até o objetivo '{objetivo}': {resultado}")
    else:
        print("Objetivo não encontrado.")
