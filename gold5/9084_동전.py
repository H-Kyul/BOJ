'''
https://www.acmicpc.net/problem/9084

# 동전 1 확장 버전
https://www.acmicpc.net/problem/2293
'''

#  제출 답안

import sys
input = sys.stdin.readline
def DP(coins):
    dp = [0]*(k+1)
    dp[0] = 1
    for value in coins:
        for i in range(value,k+1):
            dp[i] += dp[i-value]
            
    return dp[k]

for _ in range(int(input())):
    n = int(input())
    coins = list(map(int,input().split()))
    k = int(input())
    print(DP(coins))
    
