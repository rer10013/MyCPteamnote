'Longest Increasing Substring'
def LCseq(string_A, string_B, dp):
    len_A, len_B = len(string_A), len(string_B)
    
    for i in range(1, len_A + 1):
        for j in range(1, len_B + 1):
            if string_A[i - 1] == string_B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    length = dp[len_A][len_B]

    seq = [length, len_A, len_B]
    arr = []
    while seq[0] != 0:
        if dp[seq[1] - 1][seq[2]] == seq[0]:
            seq[1] -= 1
        elif dp[seq[1]][seq[2] - 1] == seq[0]:
            seq[2] -= 1
        else:
            arr.append(string_A[seq[1] - 1])
            seq = [dp[seq[1] - 1][seq[2] - 1], seq[1] - 1, seq[2] - 1]
    
    lcs = ''.join(reversed(arr))

    return dp, lcs
	

string_A = list(input())
string_B = list(input())

dp = [[0 for _ in range(len(string_B) + 1)] for _ in range(len(string_A) + 1)]
dp, arr = LCseq(string_A, string_B, dp)

print(arr)