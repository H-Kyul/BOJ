'''
https://www.acmicpc.net/problem/2231
'''

# 제출 답안
import sys
N = int(sys.stdin.readline())
for M in range(1,N+1):
    if M + sum(list(map(int,list(str(M))))) == N:
        print(M)
        break
    else:
        continue
else:
    print(0)
