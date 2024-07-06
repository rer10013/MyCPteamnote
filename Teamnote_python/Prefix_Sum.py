''' Make prefix sum array '''
def prefix_sum(): 
    summary = 0
    prefix_sum = [0]
    for i in data:
        summary += i
        prefix_sum.append(summary)
    return prefix_sum

''' Get interval sum '''
def interval_sum(left, right):
    left = 2
    right = 4
    print(prefix_sum[right] - prefix_sum[left - 1])

n = int(input())
x, y = map(int, input().split())
data = list(map(int, input().split()))
pre_sum = prefix_sum()
interval = interval_sum(x,y)