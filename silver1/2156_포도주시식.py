'''
https://www.acmicpc.net/problem/2156
'''

# 제출 답안 : deque > list 시간 감소

import sys
N = int(sys.stdin.readline())
w = [int(input()) for _ in range(N)]
if N<3:
    print(sum(w))
else:
    dp = [w[0],w[0]+w[1],max(w[0]+w[1],w[0]+w[2],w[1]+w[2])]
    for i in range(3,N):
        dp.append(max(dp[i-3]+w[i-1]+w[i], dp[i-2]+w[i], dp[i-1]))
    print(max(dp))
