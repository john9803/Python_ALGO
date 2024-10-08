# 평균
subject_cnt = int(input())
scores = list(map(int, input().split()))

M = max(scores)
for i in range(0,subject_cnt):
    scores[i] = scores[i]/M*100

avg = sum(scores)/len(scores)
print(avg)
