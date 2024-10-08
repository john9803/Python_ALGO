n,k = map(int, input().split())

coins = []
use_coin_cnt = 0

for i in range(n):
    coins.append(int(input()))

while k != 0:
    for coin in reversed(coins):
        if k/coin >= 1:
            # print(f'나누어떨어지는수 : {coin} | 개수 : {int(k/coin)}')
            use_coin_cnt += int(k / coin)
            k -= coin * int(k/coin)
        if k == 0:
            break
        # print(f'현재 k: {k}')
print(use_coin_cnt)

