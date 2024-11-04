import os
from collections import deque

os.system('cls')


class BreadthFirstAlgorithm:
    def __init__(self, grafo, inicio):
        self.grafo = grafo
        self.inicio = inicio

    def __algorithm__(self):
        visitados = set()
        fila = deque([self.inicio])

        while fila:
            vertice = fila.popleft()

            if vertice not in visitados:
                print(vertice, end=' ')
                visitados.add(vertice)
                fila.extend(self.grafo[vertice] - visitados)


if __name__ == "__main__":
    BFS = BreadthFirstAlgorithm()
    BFS.__algorithm__()
