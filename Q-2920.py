code_str = str(input()).split()

# print(code_str)

status = ''

last_code = 0

for temp in code_str:
    if not last_code == 0:
        # print('로직정상실행')
        # print(f'last_code : {last_code} | temp: {int(temp)}')
        # print(f'status : {status}')
        if int(temp) > last_code:
            if status == 'descending':
                status = 'mixed'
                break
            else:
                status = 'ascending'

        elif int(temp) < last_code:
            if status == 'ascending':
                status = 'mixed'
                break
            else:
                status = 'descending'
    last_code = int(temp)
print(status)






