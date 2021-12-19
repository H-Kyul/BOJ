# 제출 답안

import sys
N,K = map(int,sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
ans = 0
coins.sort(reverse=True)
for i in range(len(coins)):
    if coins[i] <= K:
        ans += K//coins[i]
        K = K - coins[i]* (K//coins[i])

    if K == 0 :
        break

print(ans)
