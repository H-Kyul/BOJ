'''
https://www.acmicpc.net/problem/2292
'''


# 제출 답안

import sys

N = int(sys.stdin.readline())
s,e,d = 2,6,6
if N==1:
    print(1)
else:
    for i in range(2,10**6):
        if N < s+e:
            print(i)
            break
        else:
            e += d*i
