while True:
    a, b, c = map(int, input().split())
    temp = [a, b, c]
    temp_max = max(temp)
    temp.remove(temp_max)
    temp_a = temp.pop()
    temp_b = temp.pop()

    # print(f'temp_max: {temp_max}, temp_a: {temp_a}, temp_b : {temp_b}')

    if temp_a == 0 and temp_b == 0 and temp_max == 0:
        break

    if temp_max ** 2 == temp_a ** 2 + temp_b ** 2:
        print('right')
    else:
        print('wrong')