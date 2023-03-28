class Graph:
    def __init__(self, num_vertices: int) -> None:
        self.num_vertices = num_vertices
        self.adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        
    def add_edge(self, v1: int, v2: int) -> None:
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1
        
    def remove_edge(self, v1: int, v2: int) -> None:
        if self.adj_matrix[v1][v2] == 0:
            print("Edge does not exist.")
            return
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0
        
    def dfs(self, start_vertex: int) -> None:
        visited = [False for _ in range(self.num_vertices)]
        self._dfs(start_vertex, visited)
        
    def _dfs(self, vertex: int, visited: list[bool]) -> None:
        visited[vertex] = True
        print(vertex)
        for i in range(self.num_vertices):
            if self.adj_matrix[vertex][i] == 1 and not visited[i]:
                self._dfs(i, visited)

g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(0, 4)
g.add_edge(3, 5)
g.add_edge(1, 5)
g.dfs(0)
