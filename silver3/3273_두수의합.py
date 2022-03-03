'''
https://www.acmicpc.net/problem/3273
'''

# 제출 답안

import sys
input = sys.stdin.readline
n = int(input())
arr = sorted(map(int,input().split()))
x = int(input())
cnt = 0
l,r = 0,n-1

while l<r:
    SUM = arr[l]+arr[r]
    if SUM<x:
        l+=1
        continue
    if SUM == x:
        cnt+=1
    r-=1
    
print(cnt)
