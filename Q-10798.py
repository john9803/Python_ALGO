strings = []

string_sizes = []

max_str_size = 0

results = ''

for i in range(5):
    strings.append(input())


for text in strings:
    string_sizes.append(len(text))
    for ele in text:
        if len(text) > max_str_size:
            max_str_size = len(text)

# print(f'string_sizes: {string_sizes}')

for col in range(max_str_size):
    for row in range(5):
        if col >= string_sizes[row]:
            pass
        else:
        # print(f'col: {col}, row: {row}')
            results += strings[row][col]
print(results)

