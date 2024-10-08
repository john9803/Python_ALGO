n, m = map(int, input().split(' '))

lis = list(range(1, n+1))

for _ in range(m):
    i,j = map(int, input().split(' '))

    reverse_lis = []
    for k in range(i,j+1):
        reverse_lis.append(lis[k-1])

    # print(reverse_lis)
    reverse_lis.reverse()
    # print(reverse_lis)

    for idx, w in enumerate(range(i, j+1)):
        lis[w-1] = reverse_lis[idx]
    # print(lis)

print(*lis)