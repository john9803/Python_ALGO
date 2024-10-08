# 숫자의 개수

nums = []
# 받은 문자열을 슬라이싱 해서 배열에 나누어 넣어서 수를 셀거임
# 걍 str함수써서 바로 해결했음... 함수르 잘알자
for i in range(0, 3):
    nums.append(int(input()))
result = nums[0]*nums[1]*nums[2]
num_list = list(map(int, str(result)))
cnt = []
#print(num_list)
for i in range(0,10):
    cnt.append(num_list.count(i))
    print(cnt[i])

# map 함수에 대한 심층학습 필요 -> Map함수 중요