'''
https://www.acmicpc.net/problem/3009
'''


# 제출 답안
import sys
xtics,ytics = [],[]
for _ in range(3):
    a,b = map(int,sys.stdin.readline().split())
    xtics.append(a)
    ytics.append(b)
x,y = 0,0
for i in range(3):
    if xtics.count(xtics[i])%2:
        x = xtics[i]
    if ytics.count(ytics[i])%2:
        y = ytics[i]
print(x,y)
