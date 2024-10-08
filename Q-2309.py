from itertools import combinations

tall_arr = []

real_seven = []

for i in range(9):
    tall_arr.append(int(input()))

for j in combinations(tall_arr,7):
    if sum(j) == 100:
        # print('[0] 100이 맞음')
        real_seven.append(j)
    # else:
        # print('[x] 100이 아닙니다')

if real_seven:
    for i in sorted(real_seven[0]):
        print(i)

sorted()