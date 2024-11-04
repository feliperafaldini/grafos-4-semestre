import os
from collections import deque
os.system('cls')

def depth_first_algorithm(grafo, inicio):
    visitados = set()
    fila = deque([inicio])

    while fila:
        vertice = fila.popleft()

        if vertice not in visitados:
            print(vertice, end = ' ')
            visitados.add(vertice)

            for vizinho in grafo[vertice] - visitados:
                depth_first_algorithm(grafo, vizinho, visitados)

if __name__ == "__main__":
    depth_first_algorithm()