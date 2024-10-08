from collections import deque

n,m = map(int, input().split(' '))

# 방향벡터 설정

# dy = [0,0,-1,1]
# dx = [1,-1,0,0]

dy = [1,-1,0,0]
dx = [0,0,-1,1]


boards = [input() for _ in range(n)]

chk= [[False] * m for _ in range(n)] # 지나갔는지 확인하기
chk[0][0] = True

step_cnt = 0

# 최단거리 문제 -> DFS를 염두에 두기 ( deque 이용 )


def is_valid_coord(ny,nx):
    return 0 <= ny < n and 0<= nx < m


def bfs():
    current = (0, 0, 1)

    dq = deque()
    dq.append(current)

    while dq:
        y, x, d = dq.popleft()

        # 종점 도착했을때 종료조건
        if y == n-1 and x == m-1:
            return d

        nd = d + 1
        # 4 방향 전부 탐색하기
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # ny와 nx가 유효한 좌표인지 확인하기
            if is_valid_coord(ny ,nx) and  boards[ny][nx] == '1' and chk[ny][nx] is not True:
                # print('조건만족')
                dq.append((ny, nx, nd))
                chk[ny][nx] = True

                # print(f'current_cnt = {d}')


print(bfs())


# # Q-2178 백업 -> 모범풀이
#
# # 전형적인 길찾기 문제
#
# from collections import deque
#
# # dy = (0, 1, 0, -1)
# # dx = (1, 0, -1, 0)
#
# dy = [1, -1, 0 ,0]
# dx = [0, 0, -1, 1]
#
# n, m = map(int, input().split(' '))
# board = [input() for _ in range(n)]
#
# def is_valid_coord(y, x):
#     return 0 <= y < n and 0 <= x < m
#
# def bfs():
#     chk=[[False] * m for _ in range(n)]
#     chk[0][0] = True
#     dq = deque()
#     dq.append((0,0,1))
#     cnt = 0
#     while dq:
#         print(f'현재{cnt}번째 도는중')
#         cnt += 1
#         print(dq)
#         y,x,d = dq.popleft()
#
#         if y == n - 1 and x == m - 1:
#             return d
#
#         nd = d + 1
#         for k in range(4):
#             ny = y + dy[k]
#             nx = x + dx[k]
#             if is_valid_coord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
#                 chk[ny][nx] = True
#                 dq.append((ny,nx,nd))
#
# print(bfs())