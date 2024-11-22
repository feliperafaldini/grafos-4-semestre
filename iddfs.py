import os

os.system("cls")

class IterativeDeepeningprofundidadeFirstSearch:
    def __init__(self, graph, inicio, objetivo=None):
        self.graph = graph
        self.inicio = inicio
        self.objetivo = objetivo

    def profundidadeLimitedSearch(self, vertice, objetivo, profundidade, caminho):
        caminho.append(vertice)
        if profundidade == 0:
            if vertice == objetivo:
                return caminho
            else:
                caminho.pop()
                return None
            
        if profundidade > 0:
            for neighbor in self.graph.get(vertice, []):
                result = self.profundidadeLimitedSearch(neighbor, objetivo, profundidade - 1, caminho)
                if result:
                    return result
        caminho.pop()
        return None
    
    def search(self):
        profundidade = 0
        while True:
            caminho = []
            result = self.profundidadeLimitedSearch(self.inicio, self.objetivo, profundidade, caminho)
            if result:
                return result
            profundidade += 1
        
        
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

    inicio = 'A'
    objetivo = 'Q'

    iddfs = IterativeDeepeningprofundidadeFirstSearch(grafo, inicio, objetivo)
    resultado = iddfs.search()
    
    if resultado:
        print(f"Caminho encontrado até o objetivo {objetivo}: {resultado}")
    else:
        print("Objetivo não encontrado")
