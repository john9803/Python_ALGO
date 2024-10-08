row, col = map(int, input().split())

arr = [[0 for j in range(col)] for i in range(row)]

# print(f'row: {row} | col : {col}')

res_mat = arr

for i in range(row):
    temp_row = input().split()
    for idx, j in enumerate(temp_row):
        res_mat[i][idx] += int(j)

for i in range(row):
    temp_row = input().split()
    for idx, j in enumerate(temp_row):
        res_mat[i][idx] += int(j)

arr_str = '\n'.join([' '.join(str(element) for element in row) for row in res_mat])
print(arr_str)
