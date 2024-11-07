a1, a0 = map(int, input().split(" "))

c = int(input())

n0 = int(input())

is_valid = True

def valid_func(a0, a1, n):
    return a1*n + a0

for n in range(n0, 101):
    if valid_func(a0, a1, n) <= c * n:
        pass
    else:
        is_valid = False
        break

if is_valid:
    print(1)
else:
    print(0)