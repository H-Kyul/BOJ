'''
https://www.acmicpc.net/problem/1436
'''

# 제출 답안
import sys

c = 0
n = int(sys.stdin.readline())
for i in range(10**8):
    if '666' in str(i):
        c+=1
        if c==n:
            print(i)
            break
