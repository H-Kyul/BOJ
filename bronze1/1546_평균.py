'''
https://www.acmicpc.net/problem/1546
'''

import sys

N = int(sys.stdin.readline())
s = list(map(int,sys.stdin.readline().split()))
print(sum(s)/max(s)*100/N)
