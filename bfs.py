import os
from collections import deque
os.system('cls')

def breadth_first_algorithm(grafo, inicio):
    visitados = set()
    fila = deque([inicio])

    while fila:
        vertice = fila.popleft()

        if vertice not in visitados:
            print(vertice, end = ' ')
            visitados.add(vertice)
            fila.extend(grafo[vertice] - visitados)

if __name__ == "__main__":
    breadth_first_algorithm()