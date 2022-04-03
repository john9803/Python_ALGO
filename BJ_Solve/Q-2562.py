# 최대값

box = []
for i in range(0, 9):
    box.append(int(input()))
max_num = max(box)
max_index = box.index(max_num)


print(max_num)
print(max_index+1)

# 문제를 제대로 보자! 인덱스 파악하는 문제였음.
# 일단 이번 문제로 파이썬 배열선언법, 배열입력받기, 배열의 index함수에 대해서
# 알게 되었음.