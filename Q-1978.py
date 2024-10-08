n = int(input())

cands = input().split()

count = 0

for temp in cands:
    lis = []
    for t in range(1, int(temp)+1):
        if t == 1:
            lis.append(t)
        else:
            if t%int(temp)==0:
                lis.append(t)
    if len(lis) > 2:
        count+= 1

print(count)