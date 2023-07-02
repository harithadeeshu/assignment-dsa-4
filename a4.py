from collections import defaultdict

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic(self):
        visited = set()
        current_path = set()

        for node in range(self.num_vertices):
            if node not in visited:
                if self._dfs(node, visited, current_path):
                    return True

        return False

    def _dfs(self, node, visited, current_path):
        visited.add(node)
        current_path.add(node)

        for neighbor in self.graph[node]:
            if neighbor in current_path:
                return True
            if neighbor not in visited:
                if self._dfs(neighbor, visited, current_path):
                    return True

        current_path.remove(node)
        return False

# Example usage
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

is_cycle = graph.is_cyclic()
if is_cycle:
    print("Cycle detected in the graph.")
else:
    print("No cycle detected in the graph.")
