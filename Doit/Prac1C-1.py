# 이름을 받아서 인사하기

# print 문에 조건을 넣어서 print 문과 input문 두줄로 1-1의 이름받는것을 구현했다.
print('이름을 입력하세요:', end='')
name= input()
print(f'안녕하세요? {name} 님.')

# print 문의 옵션
# end와 sep이 있다.

# end는 end='' 와 같이 표현하는데, print문의 모든 문자열이 끝나고 끝에,
# 즉 end에서 '' 따옴표 사이에 존재하는 것을 넣어준다. ( ''의 경우는 공백을 넣어준다 )

# EX) print('hi','my','name',end='')
# 출력 himyname .

# sep은 sep='' 와 같이 사용하는데, print문의 문자열이 끝날때 마다 사이사이에,
# '' 사이에 있는 것을 넣어준다. ( ''의 경우는 공백을 넣어준다.)

# EX) print('hi','my','name',sep='')
# 출력 hi my name.