'''base'''

'''
isi를 int split input으로 정의
ii를 int input으로 정의
케이스 당 값 출력이 1줄일 때 return
'''

from sys import stdin
input = stdin.readline
isi = lambda: map(int, input().rstrip().split())
ii = lambda: int(input().rstrip())

def solve():
    ans = 0

    return ans

if __name__ == '__main__':
    print(solve())