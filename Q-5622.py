dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

input_str = input()

min_time = 0

for j in input_str:
    for index, i in enumerate(dial):
        if j in i:
            min_time += (index + 3)
print(min_time)