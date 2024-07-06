''' Two_pointer Alogrithm '''
def two_pointer():
    left = 0
    right = len(arr) - 1

    while left < right:
        cur_sum = arr[left] + arr[right]

        if cur_sum == target:
            return (left + 1, right + 1)
        elif cur_sum < target:
            left += 1
        else:
            right -= 1

    return None

target = int(input())
arr = list(map(int, input().split()))
print(two_pointer())
