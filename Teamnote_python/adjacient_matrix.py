'''adjacient_matrix'''
N, M = map(int, input().split())
adj_mat = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y, weight = map(int, input().split())
    adj_mat[x][y] = weight
    adj_mat[y][x] = weight