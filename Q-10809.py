temp_str = input()

al = {'a': 0, 'b': 1, 'c':2, 'd':3, 'e':4, 'f':5, 'g': 6, 'h': 7, 'i': 8, 'j':9, 'k':10,
 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20,
 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}

find_lis = []

for a in al:
    # print(f'a: {a}')
    if a in temp_str:
        find_lis.append(temp_str.find(a))
    else:
        find_lis.append(-1)

print(*find_lis,end=' ')




