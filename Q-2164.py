from collections import deque

cards = deque(list(range(1,int(input())+1,1)))

empty_cards = True
pop_turn = True

while empty_cards:
    if len(cards) == 1:
        empty_cards = False
        break
    if pop_turn:
        cards.popleft()
        pop_turn = False
    else:
        w = cards.popleft()
        cards.append(w)
        pop_turn = True

print(cards[0])

# or you should try -> much simple
# should consider time complexity

# from collections import deque
#
# N = int(input())
# dq = deque(range(1, N+1))
# while len(dq) > 1:
#     dq.popleft()
#     dq.append(dq.popleft())
#
# print(dq.popleft())