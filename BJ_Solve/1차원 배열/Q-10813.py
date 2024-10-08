n, m = map(int, input().split(' '))

lis = list(range(1, n+1))

for _ in range(m):
    i,j = map(int, input().split(' '))

    first = lis[i-1]
    second = lis[j-1]

    lis[i-1] = second
    lis[j-1] = first

print(*lis)