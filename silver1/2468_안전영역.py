'''
https://www.acmicpc.net/problem/2468

** Hint!! 아무 지역도 물에 잠기지 않을수도 있다.
'''

# 제출 답안

import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(i,j,h):
    q = deque([[i,j]])
    visited[i][j] = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and area[nx][ny]>h and visited[nx][ny]==0:
                visited[nx][ny] = 1
                q.append([nx,ny])

n = int(sys.stdin.readline())
area = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
M = max(sum(area,[]))
ans = 0

for h in range(0,M):
    cnt = 0
    visited = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if area[i][j]>h and visited[i][j]==0:
                bfs(i,j,h)
                cnt += 1
    if cnt > ans:
        ans = cnt
print(ans)

