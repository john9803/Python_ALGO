# 걍 문자열 빼면 되자나 멍청이
t = int(input())

for case in range(t):
    test_str = input()

    isVPS = True

    stk = []

    for temp in test_str:
        if temp =='(':
            stk.append(temp)
        elif temp == ')':
            if len(stk) > 0:
                stk.pop()
            else:
                isVPS = False
                break

    if stk:
        isVPS = False
    print('YES' if isVPS else 'NO')





