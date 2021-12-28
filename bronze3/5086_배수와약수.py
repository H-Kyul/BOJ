'''
https://www.acmicpc.net/problem/5086
'''

# 제출 답안

import sys

input = sys.stdin.readline
while True:
    a,b = map(int,input().split())
    if a == b == 0:
        break
    if max(a,b)% min(a,b) == 0:
        if a>b:
            print("multiple")
        else:
            print("factor")
    else:
        print("neither")
