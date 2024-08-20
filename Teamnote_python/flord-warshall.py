''' Floyd-Warshall '''
INF = float('inf')

def floyd_warshall(): 
    for k in range(1, n + 1): # main algorithm
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1): #initialize self
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

for _ in range(m): # setting route
    a, b, c = map(int, input().split())
    graph[a][b] = c

for a in range(1, n + 1): #print result
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print('INF', end=' ') # from a to B
        else:
            print(graph[a][b], end=' ')
    print()