''' Two_pointer Alogrithm '''
def two_pointer(N, M): # N: len, M: target val
    cnt = 0
    sum = 0
    left = 0
    right = 0

    while left <= right and right < N:
        if sum >= M:
            sum -= arr[left := left+1]
            cnt += 1
        else:
            sum -= arr[right := right+1]

    return cnt

target = int(input())
arr = list(map(int, input().split()))
print(two_pointer())
