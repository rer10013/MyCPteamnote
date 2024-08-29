'''Bellman-ford (Negative edge)'''

'''
음의 간선이 존재할 때,
점 갯수: n, 간선 갯수: m, a->b cost: c
n-1번 반복하며, 모든 간선을 확인하면서 거리 확인
음수 간선 존재시 n번째에서 갱신
'''

INF = float('inf')
def bf(start):
    distance[start] = 0
    for i in range(N):
        for j in range(M):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                if i == N - 1:
                    return True
    return False

N, M = int(input())
for _ in range(M):
    a, b, c = map(int, input().split())
edges = []
distance = [INF]*(N + 1)
edges.append(a, b, c)