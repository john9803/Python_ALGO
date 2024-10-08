test_case = int(input())

for case in range(test_case):
    index = 1
    h, w, n = map(int, input().split())
    # print(f'h:{h}, w:{w}, n:{n}')
    for temp_w in range(1, w + 1):
        for temp_h in range(1, h+1):
            # print(f'index :{index}')
            # print(f'h:{temp_h}, w:{temp_w}, n:{n}')
            if index >= n:
                print(f'{temp_h*100+temp_w}')
                break
            index += 1
        if index >= n:
            break
