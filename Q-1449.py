n, l = map(int, input().split())

to_repair = [False] * 1001

holes = list(map(int,input().split()))

max_hole = max(holes)

for i in holes:
    to_repair[i] = True

current = 0
used_tape = 0

while current != 1001:
    if to_repair[current]:
        current += l
        used_tape += 1
    else:
        current += 1

    # print(f'current: {current} | user_tape: {used_tape} ')
    if current > max_hole:
        break

print(used_tape)


