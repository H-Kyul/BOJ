'''
https://www.acmicpc.net/problem/1009
'''

# 제출 답안

import sys
import math
for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    if M % 4:
        M %= 4
    else:
        M = 4
    res = math.pow(N,M)%10

    if res:
        print(int(res))
    else:
        print(10)
