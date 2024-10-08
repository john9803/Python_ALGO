
# 연결이 되어있는가만 파악하면 됨

n, m  = map(int,input().split(' '))

matrix = [[0] * n for i in range(n)]

# link_list = [[0] * n]

for i in range(m):
    u, v = map(int, input().split(' ')) # 백준에서 제출할때는 input 쓰면 시간초과 발생
    matrix[u-1][v-1] = matrix[v-1][u-1] = 1
# print(matrix)

ans = 0
chk = [False] * n

def dfs(now):
    for nxt in range(n):
        if matrix[now][nxt] and not chk[nxt]:
            chk[nxt] = True
            dfs(nxt)
            # print(f'dfs({nxt}) 로 이동')

for i in range(n):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)




