'''
https://www.acmicpc.net/problem/4796
'''

# 제출 답안
import sys
i = 1
while True:
    l,p,v = map(int,sys.stdin.readline().split())
    if l == 0:
        break
    print(f'Case {i}: {(v//p)*l+min(l,v%p)}')
    i+=1
