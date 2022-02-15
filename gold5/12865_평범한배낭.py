'''
https://www.acmicpc.net/problem/12865
'''

# 제출 답안

import sys

def knapsack(N,K):
    for n in range(1,N+1):
        w,v = map(int,sys.stdin.readline().split())
        for k in range(1,K+1):
            if w <= k: 
                dp[n][k] = max(dp[n-1][k-w]+v,dp[n-1][k])
            else:
                dp[n][k] = dp[n-1][k]
    return dp[N][K]
N,K = map(int,sys.stdin.readline().split())
dp = [[0]*(K+1) for _ in range(N+1)]
print(knapsack(N,K))
