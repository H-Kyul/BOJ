'''
https://www.acmicpc.net/problem/1193
'''

# 제출 답안

import sys
N = int(sys.stdin.readline())
for i in range(1,N+1):
    if N <= sum(range(1,i+1)):
        idx = N- sum(range(1,i))
        a,b = idx,i+1-idx

        if i%2 != 0:
            a,b = b,a
        print(f'{a}/{b}')
        break
