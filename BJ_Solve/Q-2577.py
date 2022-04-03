# 숫자의 개수

nums = []
# 받은 문자열을 슬라이싱 해서 배열에 나누어 넣어서 수를 셀거임
# 걍 str함수써서 바로 해결했음... 함수르 잘알자
for i in range(0, 3):
    nums.append(int(input()))
result = list(int(str(nums[0]*nums[1]*nums[2])))
count_num = []
for i in range(0,10):
    count_num.append(result.count(i))
    print(count_num[i])
print(result)
print(type(result[0]))
#print()
