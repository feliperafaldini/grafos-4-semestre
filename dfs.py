import os

os.system("cls")


class DepthFirstAlgorithm:
    def __init__(self, grafo, inicio):
        self.grafo = grafo
        self.inicio = inicio

    def algorithm(self, vertice, visitados, arvore):

        if vertice not in visitados:
            visitados.add(vertice)
            arvore[vertice] = []

            for vizinho in self.grafo[vertice]:
                if vizinho not in visitados:
                    arvore[vertice].append(vizinho)
                    self.algorithm(vizinho, visitados, arvore)

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

    DFS = DepthFirstAlgorithm(grafo, inicio)
    visitados = set()
    arvore = {}

    DFS.algorithm(inicio, visitados, arvore)
