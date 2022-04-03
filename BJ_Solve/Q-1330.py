# 단계별로 풀어보기 조건문

# input함수의 option지정
# map 함수로 다중입력을 받음. 첫번째 인자는 데이터 타입, 두번째는 input메소드임
# split이라는 메소드로 공백단위로 나누어서 입력을 받음.

A, B = map(int, input("두개의 숫자를 입력하세요: ").split())
#print(A,B)

if A-B > 0:
    print(">")
if A-B < 0:
    print("<")
if A-B == 0:
    print("==")
