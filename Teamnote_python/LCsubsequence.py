'Longest Increasing Substring'
def LCseq(string_A, string_B, dp):
    seq = [0, 0, 0]
    for i in range(len(string_A)):
        for j in range(len(string_B)):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif string_A[i] == string_B[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] >= seq[0]:
                    seq = [dp[i][j], i, j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    arr = []
    while seq[0] != 0:
        if dp[seq[1]-1][seq[2]] == seq[0]:
            seq[1] -= 1
        elif dp[seq[1]][seq[2]-1] == seq[0]:
            seq[2] -= 1
        else:
            arr.append(string_A[seq[1]])
            seq = [i - 1 for i in seq]

    arr = ''.join(reversed(arr))

    return dp, arr
	

string_A = list(input())
string_B = list(input())

dp = [[0 for _ in range(len(string_B))] for _ in range(len(string_A))]
dp, arr = LCseq(string_A, string_B, dp)

print(arr)