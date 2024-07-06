''' GCD (Greatest Common Divisor) '''
def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b

''' LCM (Least Common Multiple) '''
def lcm(a, b):
    return a * b // gcd(a, b)

x, y = map(int, input().split())
print(gcd(x, y))
print(gcd(x, y))