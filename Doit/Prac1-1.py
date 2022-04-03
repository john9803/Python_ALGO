# 3개의 정수를 입력받아서 최댓값을 구하는 코드를 작성합시다.

print('3개 정수의 최댓값을 구합니다')

# input으로 값을 입력받은 뒤, 그 값의 자료형을 int형으로 강제로 바꾸어서 a에 할당함.
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

# 일단 a를 max로 정해두고 조건문을 활용해서 maximum값을 변화시킴, if 와 :(콜론) 사이에 있는것이 조건식이다.
maximum = a
# b가 maximum보다 크다면 maximum의 값을 b의 들어있는 값으로 바꾸시오 -> 조건식 b > maximum
if b > maximum: maximum=b
# c가 maximum보다 크다면 maximum의 값을 c의 들어있는 값으로 바꾸시오
if c > maximum: maximum=c

# print 함수 안에 존재하는 f는 f-string formatting 이라는 기능이다.
print(f'최댓값은 {maximum}입니다.')

# f-string formatting
# f를 문자열 앞에 적어주고, 그안에 중괄호를 사용해서 변수를 집어넣을 수 있다.
# 위에서는 maximum이라는 변수를 문자열 속에다가 집어넣은 것이다.

# input() 함수는 괄호안에 문자열을 출력할 수 있는 기능도 들어있다.