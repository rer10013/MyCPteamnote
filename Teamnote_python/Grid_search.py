'''grid search (NEWS) '''
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# case dfs
''' Depth First Search (DFS) '''
def dfs(dot):
    #print(x, end=' ') #print lines
    x, y = dot
    visited.add((x, y))
    for i, j in zip(dx, dy):
        nx = dx + x
        ny = dy + y
        if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
            dfs(x, y)

n, m, start = map(int, input().split()) #input. n = columns, m = rows
graph = [list(map(int, input())) for _ in range(m)]
visited = set()
dfs(start)