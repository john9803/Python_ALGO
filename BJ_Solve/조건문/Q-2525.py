# 오븐시계

A, B = map(int, input().split())
C = int(input())
hour = int(C/60)
min = int(C%60)
#print(hour,min)
#print(A,B,C)

if B+min>=60:
    B += min
    B %= 60
    A += 1
    if A+hour>=24:
        A += hour
        A %= 24
    else:
        A += hour
else:
    A %= 24
    B += min
    if A+hour>=24:
        A += hour
        A %= 24
    else:
        A += hour

print(A,B)

# 피드백 -> 처음에는 A 조건 안에 B를 넣었는데,
# 선후관계를 생각했을 때 B에서 올림하는 것이 선행되야하는
# 구조라서 B 조건 안에 A 조건을 넣는 형태로 바꾸었다.
