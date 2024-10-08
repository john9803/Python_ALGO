n = int(input())

sizes = list(map(int, input().split()))

# print(sizes)

t, p = map(int, input().split())

num_t = 0
num_p = 0
num_p_sol = 0

for i in sizes:
    # print(f'{i//t}')
    if i%t == 0:
        num_t += i // t
    else:
        num_t += (i // t) + 1
num_p = n//p
num_p_sol = n%p

print(num_t)
print(f'{num_p} {num_p_sol}')

