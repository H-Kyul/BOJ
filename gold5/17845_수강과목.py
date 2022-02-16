'''
https://www.acmicpc.net/problem/17845
'''

# 제출 답안 2 - 1차원 리스트

import sys
input = sys.stdin.readline
def knapsack(K,N):
    dp = [0]*(K+1)
    for n in range(1,N+1):
        im,tm = map(int,input().split())
        for k in range(tm,K+1)[::-1]:
            dp[k] = max(dp[k],dp[k-tm]+im)
    return dp[K]

K,N = map(int,input().split())
print(knapsack(K,N))

# 제출 답안 1 - 2차원 리스트

import sys
input = lambda : map(int,sys.stdin.readline().split())
def knapsack(K,N):
    dp = [[0]*(K+1) for _ in range(N+1)]
    for n in range(1,N+1):
        im,tm = input()
        for k in range(1,K+1):
            if tm <= k:
                dp[n][k] = max(dp[n-1][k-tm]+im,dp[n-1][k])
            else:
                dp[n][k] = dp[n-1][k]
    return dp[N][K]

K,N = input()
print(knapsack(K,N))
