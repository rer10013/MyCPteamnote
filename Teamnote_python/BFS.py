''' Breadth First Search (BFS) '''

'''
deque 이용한 BFS, que에 업데이트 하면서 간 것으로 처리
n: 정점수, m: 간선 수, start: 시점, x, y: 간선
print문 이동 경로 표시
'''

from collections import deque as deq

def bfs(x):
    q = deq([x])
    visited[x] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for y in graph[x]:
            if not visited[y]:
                q.append(y)
                visited[y] = True

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for e in graph:
    e.sort()

visited = [False] * (n + 1)
bfs(start)