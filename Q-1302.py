N = int(input())

book_count = {}

# 찾을것 -> 책이름 최소정렬값, 팔린책개수(음수처리해서 max_heap처리하게 만들기 -> heap 필요없음 )

# input = sys.stdin.readline()
for i in range(1, N+1):
    book = str(input())
    if book in book_count:
        book_count[book] += 1
    else:
        book_count[book] = 1
    # print(book_count)
max_value = max(book_count.values())

max_keys = []
for k, v in book_count.items():
    if v == max_value:
        max_keys.append(k)

print(sorted(max_keys)[0])

