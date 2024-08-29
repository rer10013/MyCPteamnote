'''adjacient_matrix'''

'''
인접한 리스트를 인덱스를 이용한 2차원 그리드로
'''

N, M = map(int, input().split())
adj_mat = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y, weight = map(int, input().split())
    adj_mat[x][y] = weight
    adj_mat[y][x] = weight