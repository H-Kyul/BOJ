'''
https://www.acmicpc.net/problem/1182
'''

# 제출답안
import sys
def subset(i, total):
    global cnt
    if i == n:
        return
    subset(i+1,total+arr[i])
    subset(i+1,total)
    if total+arr[i] == s:
        cnt+=1
       
n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0      
subset(0,0)
print(cnt)
