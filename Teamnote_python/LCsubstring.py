'Longest Increasing Substring'
def LCstr(string_A, string_B, dp):
    for i in range(string_A):
        if i in string_B:
            break
    else:
        return dp, ''
    
    seq = [0, 0, 0]
    for i in range(len(string_A)):
        for j in range(len(string_B)):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif string_A[i] == string_B[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > seq[0]:
                    seq = [dp[i][j], i, j]
            else:
                dp[i][j] = 0
                
    end_index = seq[1]
    length = seq[0]
    arr = ''.join([string_A[i] for i in range(end_index - length + 1, end_index + 1)])
    
    return dp, arr
	

string_A = list(input())
string_B = list(input())

dp = [[0 for _ in range(len(string_B))] for _ in range(len(string_A))]
dp, arr = LCstr(string_A, string_B, dp)
print(arr)