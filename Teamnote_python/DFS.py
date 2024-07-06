''' Depth First Search (DFS) '''
def dfs(x):
    #print(x, end=' ') #print lines
    visited[x] = True
    for y in graph[x]:
        if not(visited[y]):
            dfs(y)

n, m, start = map(int, input().split()) #input. n = dots, m = lines
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for e in graph:
    e.sort()

visited = [False] * (n + 1)
dfs(start)