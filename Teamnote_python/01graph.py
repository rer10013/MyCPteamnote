'''edge case: graphweight is 0 or 1'''
from collections import deque

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]
    
    def add_edge(self, u, v, weight):
        self.adj_list[u].append((v, weight)) # undirected
    
    def bfs_01(self, src):
        dist = [float('inf')] * self.num_vertices # Init distance infinity
        dist[src] = 0

        dq = deque([src]) # Init deque with source
        while dq:
            u = dq.popleft()
            for v, weight in self.adj_list[u]:
                if weight == 0 and dist[v] > dist[u]:
                    dist[v] = dist[u]
                    dq.appendleft(v)
                elif weight == 1 and dist[v] > dist[u] + 1:
                    dist[v] = dist[u] + 1
                    dq.append(v)

        return dist

n, m = map(int, input().split()) # n = dots, m = lines
graph = Graph(n) # num of dots
for _ in range(m):
    u, v, w = map(int, input().split())
    Graph.add_edge(u, v, w)

    src = 0
    distances = graph.bfs_01(src)
    print(distances)
