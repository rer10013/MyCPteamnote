''' Depth First Search (DFS) '''

'''
BFS와 입력처리 같음, 출력 같음
재귀 많이 들어가는 경우:
sys.setrecursionlimit(10**5)
이 이상 경우 보통 BFS
재귀 시작하면서 간 것으로 처리
'''

def dfs(x):
    print(x, end=' ')
    visited[x] = True
    for y in graph[x]:
        if not(visited[y]):
            dfs(y)

n, m, start = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for e in graph:
    e.sort()

visited = [False] * (n + 1)
dfs(start)