''' Longest increasing Sequence '''
from bisect import bisect_left

def longest_increasing_subsequence(graph):
    previous = [None] * n
    indice = [None]
    min_tail = [float('-inf')] # - infinity
    for i in range(n):
        if graph[i] > min_tail[-1]:
            previous[i] = indice[-1]
            indice.append(i)
            min_tail.append(graph[i])
        else:
            # binary search
            k = bisect_left(min_tail, graph[i])
            indice[k] = i
            min_tail[k] = graph[i]
            previous[i] = indice[k - 1]
        
        # extract sol reverse order
        q = indice[-1]
        s = []
        while q is not None:
            s.append(graph[q])
            q = previous[q]
    return s[::-1] # sol

n = int(input())
graph = list(map(int, input().split()))