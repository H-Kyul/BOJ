'''
https://www.acmicpc.net/problem/1764
'''

# 제출 답안

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
P = list(input().rstrip() for _ in range(N+M))
ans = sorted(set(P[:N])&set(P[N:]))
print(len(ans),*ans,sep='\n')
