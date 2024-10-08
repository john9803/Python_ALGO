num = int(input())

for i in range(num):
    stk = 0
    score = 0
    inputs = input()
    for j in inputs:
        if j == "O":
            stk += 1
        else:
            stk = 0
        if j == "O":
            score += stk
    print(score)





