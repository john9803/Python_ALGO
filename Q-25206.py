scores = []
tran_score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

for _ in range(20):
    scores.append(input().split(' '))
# print(scores)

score_sum = 0
subject_cnt = 0

for score_list in scores:
    cnt = float(score_list[1])
    if score_list[2] == 'P':
        pass
    else:
        score_sum += (tran_score[score_list[2]] * cnt)
        subject_cnt += cnt
print(round(score_sum/subject_cnt, 6)) # 포매팅 해야함

# print('{:.6f}'.format(score_sum/subject_cnt))