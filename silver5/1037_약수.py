'''
https://www.acmicpc.net/problem/1037
'''

# 제출 답안

import sys
input = sys.stdin.readline

a = int(input())
div = sorted(map(int,input().split()))

if a % 2 == 0:
    print(div[0]*div[a-1])
else:
    print(div[a//2]**2)
