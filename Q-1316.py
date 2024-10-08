word_cnt = int(input())

cont_flag = 0

cont_cnt = word_cnt

for _ in range(word_cnt):
    text = input()
    has_error = False
    for idx in range(len(text)-1):
        if text[idx] == text[idx+1]:
            pass
            # print('정상케이스')
        elif text[idx] in text[idx+1:]:
            # print('연속문자 아님')
            cont_cnt -= 1
            break

print(cont_cnt)





