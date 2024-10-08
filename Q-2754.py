grade = input()

point = 0

str_dic = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
variation_dic = {'+': 0.3, '-': -0.3, '0': 0.0}

point += str_dic[grade[0]]
if len(grade) > 1:
    point += variation_dic[grade[1]]
print(point)