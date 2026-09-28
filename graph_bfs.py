from collections import deque

class Graph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs(self, start):
        visited = {start}
        order = []
        queue = deque([start])

        while queue:
            u = queue.popleft()
            order.append(u)
            for v in self.adj[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)

        return order
    
g1 = Graph()

g1.add_edge("A", "B")
g1.add_edge("A", "C")
g1.add_edge("B", "D")
g1.add_edge("C", "E")

print("Test 1: connected graph")
print("BFS from A: ", g1.bfs("A"))
print("BFS from E: ", g1.bfs("E"))


g2 = Graph()
g2.add_edge("A", "B")
g2.add_edge("B", "C")
g2.add_edge("D", "E")

print("Test 2: disconnected from graph")
print("BFS from A: ", g2.bfs("A"))
print("BFS from D: ", g2.bfs("D"))


g3 = Graph()
g3.add_edge("A", "B")
g3.add_edge("A", "C")
g3.add_edge("B", "D")
g3.add_edge("C", "D")
g3.add_edge("D", "E")
g3.add_edge("E", "F")

print("Test 3: six vertex graph with a cycle")
print("BFS from A:", g3.bfs("A"))
print("BFS from F:", g3.bfs("F"))