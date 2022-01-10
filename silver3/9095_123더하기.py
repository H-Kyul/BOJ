'''
https://www.acmicpc.net/problem/9095
'''

# 제출 답안
import sys
dp = [0]*11
dp[1],dp[2],dp[3] = 1,2,4
for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    for i in range (4,N+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[N])
