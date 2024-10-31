# 색종이의 수
p_cnt = int(input())

dx = [0,  0, 10, 10]
dy = [0, 10, 10, 0 ]



boards = []

dup_boards = []

colored_area = 300

for _ in range(p_cnt):
    x, y = map(int, input().split(' '))
    boards.append((x,y))


for first_idx, first_rec in enumerate(boards): # 점검좌표
    for sec_idx, sec_rec in enumerate(boards): # 피점검좌표
        if first_idx == sec_idx:
            pass

        # 4점이 해당 종이안에 존재하는지 확인
        for d in range(4):
            temp_x = first_rec[0] + dx[d]
            temp_y = first_rec[1] + dy[y]

            temp_res = [0,0]

            if sec_rec[0] < temp_x < sec_rec[0]+10:



            if sec_rec[1] < temp_y < sec_rec[1]+10:










