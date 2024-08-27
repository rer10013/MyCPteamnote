'''Prim algorithm(greedy approach)'''
INF = float('inf')

def prim(start): #use when N << M, O(N^2)
    global N, adj_mat
    visited_set = set()
    visited_set.add(start)
    distance = 0

    for _ in range(N - 1):
        min_dist, next_node = INF, -1

        for node in visited_set:
            for j in range(1, N + 1):
                if j not in visited_set and 0 < adj_mat[node][j] < min_dist:
                    min_dist = adj_mat[node][j]
                    next_node = j

        distance += min_dist
        visited_set.add(next_node)

    return distance



N, M = map(int, input().split())
adj_mat = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y, weight = map(int, input().split())
    adj_mat[x][y] = weight
    adj_mat[y][x] = weight

print(prim(1))
