''' Dijkstra Shortest Path '''
import heapq
INF = float('inf')

def dijkstra(start):
    q = [(0, start)]
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m = map(int, input().split()) # n = dots, m = nodes
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split()) # a = start, b = end, c = cost
    graph[a].append((b, c))

dijkstra(start)

for i in range(1, n + 1): # from start to i
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])