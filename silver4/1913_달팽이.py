'''
https://www.acmicpc.net/problem/1913
'''
# 제출 답안

import sys
n = int(sys.stdin.readline())
target = int(sys.stdin.readline())
arr = [[0] * n for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
x,y = 0,0
cnt = n**2
d = 0
x_,y_ = 0,0

while cnt>0:
    arr[x][y] = cnt
    if cnt == target:
        x_,y_ = x+1,y+1
    cnt-=1
    nx = x+dx[d]
    ny = y+dy[d]
    if nx < 0 or nx >= n or ny <0 or ny >= n or arr[nx][ny]!=0:
        d = (d+1)%4
        nx = x+dx[d]
        ny = y+dy[d]
    x,y = nx,ny

for row in arr:
    print(*row)
print(x_, y_)
