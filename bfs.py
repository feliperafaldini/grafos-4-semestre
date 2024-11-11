import os
from collections import deque

os.system("cls")


class BreadthFirstAlgorithm:
    def __init__(self, grafo, inicio):
        self.grafo = grafo
        self.inicio = inicio

    def algorithm(self):
        visitados = set()
        fila = deque([self.inicio])
        arvore = {}

        while fila:
            vertice = fila.popleft()

            if vertice not in visitados:
                visitados.add(vertice)
                arvore[vertice] = []
                for vizinho in self.grafo[vertice]:
                    if vizinho not in visitados:
                        fila.append(vizinho)
                        arvore[vertice].append(vizinho)

                self.print(arvore)

    def print(self, arvore):
        os.system("cls")
        for vertice, filhos in arvore.items():
            print(f"{vertice} -> {filhos}")


if __name__ == "__main__":
    grafo = {
        "A": {"B", "C"},
        "B": {"A", "D", "E"},
        "C": {"A", "F"},
        "D": {"B"},
        "E": {"B", "F"},
        "F": {"C", "E"},
    }

    inicio = "A"

    BFS = BreadthFirstAlgorithm(grafo, inicio)
    BFS.algorithm()
