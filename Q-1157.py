import sys

# input = sys.stdin.readline()
text = input()

text_dict = {}

text = text.upper() # 대문자 통일

for ele in text:
    if ele in text_dict:
        text_dict[ele] += 1
    else:
        text_dict[ele] = 1

max_rep_num = max(text_dict.values())

max_key = ''
max_keys = []


for k, v in text_dict.items():
    if v == max_rep_num:
        max_keys.append(k)

if len(max_keys) > 1:
    print('?')
else:
    print(max_keys[0])
