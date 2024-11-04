import os
from collections import deque

os.system('cls')


class DepthFirstAlgorithm:
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

                for vizinho in self.grafo[vertice] - visitados:
                    self.__algorithm__(self.grafo, vizinho, visitados)


if __name__ == "__main__":
    DFS = DepthFirstAlgorithm()
    DFS.__algorithm__()
