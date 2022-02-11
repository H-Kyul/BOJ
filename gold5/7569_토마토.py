'''
https://www.acmicpc.net/problem/7569
'''

# 제출 답안

import sys
from collections import deque
def bfs(queue,chk):
    while q:
        f,x,y = q.popleft()

        df = [0,0,0,0,1,-1]
        dx = [-1,1,0,0,0,0]
        dy = [0,0,-1,1,0,0]    
        for k in range(6):
            nf = f + df[k]; nx = x + dx[k]; ny = y + dy[k]

            if 0<=nf<h and 0<=nx<m and 0<=ny<n and box[nf][nx][ny]==0:
                box[nf][nx][ny] = box[f][x][y] +1
                q.append([nf,nx,ny])
                chk-=1

    if chk != 0:  # 안익은(0) 토마토가 있음
        return -1
    return box[f][x][y]-1

n,m,h = map(int, sys.stdin.readline().split())
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(m)] for _ in range(h)]
q = deque([])
chk = 0
for f in range(h):
    for i in range(m):
        for j in range(n):
            if box[f][i][j] == 1:
                q.append([f,i,j])
            elif box[f][i][j] == 0:
                chk += 1
if chk == 0:
    print(0)
    exit(0)
    
print(bfs(q,chk))
