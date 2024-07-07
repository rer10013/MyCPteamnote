''' Knapsack '''
def knapsack():
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(K+1):
            if clist[i] <= j:
                dp[i][j] = max(vlist[i]+dp[i-1][j-clist[i]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][K]


N, K = map(int,input().split())
vlist = [0]
clist = [0]
for i in range(N):
    iC, iV = map(int, input().split())
    vlist.append(iV)
    clist.append(iC)

print(knapsack())