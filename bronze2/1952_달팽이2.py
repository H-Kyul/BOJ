'''
https://www.acmicpc.net/problem/1952
'''

# 제출 답안

import sys
m,n = map(int,sys.stdin.readline().split())
arr = [[0]*n for _ in range(m)]
x,y,d = 0,0,0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
cnt = 0

while arr[x][y]==0:
    arr[x][y] = 1
    nx = x+dx[d]
    ny = y+dy[d]

    if nx<0 or nx>=m or ny<0 or ny>=n or arr[nx][ny]!=0:
        d = (d+1)%4
        nx = x+dx[d]
        ny = y+dy[d]
        cnt+=1
    x,y = nx,ny
print(cnt-1)
