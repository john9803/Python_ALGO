c_words = ["c=", 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

c_cnt = 0

text = input()
for word in c_words:
    if word in text:
        c_cnt += 1
        print(f'현재 cnt -> {c_cnt}')
    else:
        print('검출X')

print(c_cnt)

