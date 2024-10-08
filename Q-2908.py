# ''.join(['s'.'t'.'r'] 이 주요한 아이디어임

a,b = map(int, input().split(' '))

a_ = str(a)
a__ = list(a_)
a__.reverse()

new_a = ''.join(a__)
# print(f'new_a{new_a}')

b_ = str(b)
_b = list(b_)
_b.reverse()
new_b = ''.join(_b)


# print(f'new_b{new_b}')

if new_a > new_b:
    print(new_a)
else:
    print(new_b)