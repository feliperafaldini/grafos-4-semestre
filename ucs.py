import heapq


class UniformCostSearch:
    def __init__(self, graph):
        self.graph = graph

    def search(self, start, goal):
        frontier = []
        heapq.heappush(frontier, (0, start))

        min_cost = {start: 0}

        came_from = {}

        while frontier:
            current_cost, current_node = heapq.heappop(frontier)

            if current_node == goal:
                path = self._reconstruct_path(came_from, start, goal)
                return min_cost[goal], path

            for neighbor, edge_weight in self.graph[current_node]:
                new_cost = current_cost + edge_weight

                if neighbor not in min_cost or new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    heapq.heappush(frontier, (new_cost, neighbor))
                    came_from[neighbor] = current_node

    def _reconstruct_path(self, came_from, start, goal):
        path = [goal]
        while path[-1] != start:
            current_node = path[-1]
            path.append(came_from[current_node])
        path.reverse()
        return path


if __name__ == "__main__":
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("A", 1), ("C", 2), ("D", 5)],
        "C": [("A", 4), ("B", 2), ("D", 1)],
        "D": [("B", 5), ("C", 1)],
    }

    ucs = UniformCostSearch(graph)

    start_node = "A"
    goal_node = "D"

    cost, path = ucs.search(start_node, goal_node)

    print(f"Custo mínimo: {cost}")
    print(f"Caminho: {path}")
