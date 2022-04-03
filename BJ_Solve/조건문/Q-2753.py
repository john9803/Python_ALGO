# Yoon Year detecter

y_year = int(input())
#print(y_year)
if y_year%4==0 and y_year%100!=0 or y_year%400==0:
    print("1")
else:
    print("0")