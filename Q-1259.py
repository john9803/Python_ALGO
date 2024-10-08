

while True:
    test_str = input()

    if test_str == '0':
        break

    seed = int(len(test_str) / 2)

    is_odd = bool(len(test_str) % 2)

    is_pel = True

    if is_odd:
        # print('홀수입니다')
        for i in range(seed):
            if test_str[i] != test_str[-(i + 1)]:
                # print('두 수가 같습니다')
                # print('두 수가 같지 않습니다')
                is_pel = False
                break
            # print(f'test_str[{i}]:{test_str[i]} , test_str[{-(i + 1)}]:{test_str[-(i + 1)]}')

    else:
        # print('홀수가 아닙니다')
        for i in range(seed):
            if test_str[i] != test_str[-(i + 1)]:
                # print('두 수가 같습니다')
                # print('두 수가 같지 않습니다')
                is_pel = False
                break
            # print(f'test_str[{i}]:{test_str[i]} , test_str[{-(i + 1)}]:{test_str[-(i + 1)]}')

    if is_pel:
        print('yes')
    else:
        print('no')