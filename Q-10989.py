# 아무래도 정렬방식이 너무 오래걸려서 그런것 같음.
# 정렬로직은 한번만 실행시키는 것으로 해야겠다.
n = int(input())

cnt_arr = []

for i in range(n):
    # print(f'{i} 숫자 차례')
    cnt_arr.append(int(input()))

print(f'입력받은 배열 : {cnt_arr}')

for idx, cand in enumerate(cnt_arr):
    if cand > max(cnt_arr):
        cnt_arr.append(cand)
        break

    # print(f'cnt_arr{idx} 번째 반복')
    # if cand <= j:
    #     cnt_arr.insert(idx, cand)
    #     break


            # print(f'max_cnt = {max(cnt_arr)}')
            # print(f'idx:{idx},arr: {cnt_arr[idx]} cand: {cand}')
# print(cnt_arr)
for i in cnt_arr:
    print(i)


