'''
https://www.acmicpc.net/problem/2293
'''

# 제출 답안

import sys
n,k = map(int,sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
dp = [0]*k
for i in range(n):
    value = coins[i]
    if value <= k:
        dp[value-1] +=1
    for j in range(value,k):
        dp[j] += dp[j-value]
print(dp[k-1])
