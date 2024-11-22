import os

os.system("cls")

class DepthFirstAlgorithm:
    def __init__(self, grafo, inicio, objetivo = None):
        self.grafo = grafo
        self.inicio = inicio
        self.objetivo = objetivo

    def depthFirstSearch(self, vertice, objetivo, caminho, visitados):
        caminho.append(vertice)
        visitados.add(vertice)

        if vertice == objetivo:
            return caminho
        
        for vizinho in self.grafo[vertice]:
            if vizinho not in visitados:
                resultado = self.depthFirstSearch(vizinho, objetivo, caminho, visitados)
                if resultado:
                    return resultado
                
        caminho.pop()
        return None
    
    def search(self):
        caminho = []
        visitados = set()
        resultado = self.depthFirstSearch(self.inicio, self.objetivo, caminho, visitados)
        return resultado
        
if __name__ == "__main__":
    grafo = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': ['J'],
    'F': [],
    'G': ['K'],
    'H': ['L'],
    'I': ['M', 'N'],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': ['O', 'P'],
    'O': [],
    'P': ['Q'],
    'Q': []
    }

    inicio = "A"
    objetivo = "Q"

    dfs = DepthFirstAlgorithm(grafo, inicio, objetivo)
    resultado = dfs.search()

    if resultado:
        print(f"Caminho encontrado até o objetivo {objetivo}: {resultado}")
    else:
        print("Objetivo não encontrado.")