import os

os.system("cls")


class UniformCostSearch:
    def __init__(self, grafo):
        self.grafo = grafo

    def uniformCostSearch(self, inicio, objetivo, visitados, custo_minimo, anterior):
        fila = [(0, inicio)]
        custo_minimo[inicio] = 0

        while fila:
            fila.sort()
            custo_atual, vertice_atual = fila.pop(0)

            if vertice_atual == objetivo:
                caminho = self._caminho(anterior, inicio, objetivo)
                return custo_minimo[objetivo], caminho

            if vertice_atual not in visitados:
                visitados.add(vertice_atual)

                for vizinho, peso_aresta in self.grafo[vertice_atual]:
                    novo_custo = custo_atual + peso_aresta

                    if (
                        vizinho not in custo_minimo
                        or novo_custo < custo_minimo[vizinho]
                    ):
                        custo_minimo[vizinho] = novo_custo
                        fila.append((novo_custo, vizinho))
                        anterior[vizinho] = vertice_atual

        return None, []

    def search(self, inicio, objetivo):
        visitados = set()
        custo_min = {}
        anterior = {}

        return self.uniformCostSearch(inicio, objetivo, visitados, custo_min, anterior)

    def _caminho(self, anterior, inicio, objetivo):
        caminho = [objetivo]
        while caminho[-1] != inicio:
            no_atual = caminho[-1]
            caminho.append(anterior[no_atual])

        caminho.reverse()
        return caminho


if __name__ == "__main__":
    grafo = {
        "A": [("B", 3), ("C", 6), ("D", 1)],
        "B": [("A", 3), ("C", 2), ("E", 5)],
        "C": [("A", 6), ("B", 2), ("D", 4), ("F", 1)],
        "D": [("A", 1), ("C", 4), ("G", 7)],
        "E": [("B", 5), ("F", 2), ("H", 3)],
        "F": [("C", 1), ("E", 2), ("I", 4)],
        "G": [("D", 7), ("J", 2)],
        "H": [("E", 3), ("I", 6), ("J", 1)],
        "I": [("F", 4), ("H", 6), ("K", 2)],
        "J": [("G", 2), ("H", 1), ("L", 8)],
        "K": [("I", 2), ("L", 5)],
        "L": [("J", 8), ("K", 5), ("M", 2)],
        "M": [("L", 2), ("N", 3)],
        "N": [("M", 3), ("O", 6)],
        "O": [("N", 6), ("P", 1)],
        "P": [("O", 1), ("Q", 3)],
        "Q": [("P", 3), ("R", 2)],
        "R": [("Q", 2), ("S", 4)],
        "S": [("R", 4), ("T", 3)],
        "T": [("S", 3), ("U", 2)],
        "U": [("T", 2), ("V", 5)],
        "V": [("U", 5), ("W", 1)],
        "W": [("V", 1), ("X", 2)],
        "X": [("W", 2), ("Y", 3)],
        "Y": [("X", 3), ("Z", 4)],
        "Z": [("Y", 4)],
    }

    ucs = UniformCostSearch(grafo)

    inicio = "A"
    objetivo = "Z"

    custo, caminho = ucs.search(inicio, objetivo)

    if caminho:
        print(f"Custo Mínimo: {custo}\nCaminho encontrado até o objetivo {objetivo}: {caminho}")
    else:
        print("Objetivo não encontrado")
