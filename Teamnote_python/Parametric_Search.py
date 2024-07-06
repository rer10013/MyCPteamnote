''' Parametric_Search (uses binary search) '''
def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        if solve(mid):
            end = mid - 1
        else:
            start = mid + 1
    return mid

def solve(mid):
    return True

n = int(input())
array = list(map(int, input().split()))

result = binary_search(0, n - 1)
print(result)