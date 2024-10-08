# 나머지
num_cnt = []
residue_cnt = []

for i in range(0,10):
    num_cnt.append(int(input()))
    residue_cnt.append(num_cnt[i]%42)
residue_new = list(set(residue_cnt))
print(len(residue_new))

# "배열의 중복" 을 없애기 위해서 set이라는 함수 이용.
# 집합의 개념으로 중복되는 것이 없어지고 그것을 다시 리스트로 바꿈.

