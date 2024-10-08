from math import gcd

a, b = map(int, input().split())  # 두 수 입력
result = gcd(a, b)

print(result)

from math import lcm

result = lcm(a, b)

print(result)