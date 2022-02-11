'''
https://www.acmicpc.net/problem/7576
'''

# 제출 답안

import sys
from collections import deque

def bfs(i, j):
    day = 1
    while q:
        x, y = q.popleft()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if box[nx][ny] == 0:
                    q.append([nx, ny])
                    box[nx][ny] = box[x][y] + 1
                    if box[nx][ny] > day:
                        day = box[nx][ny]
    for i in box:
        if 0 in i:
            return -1
    return day - 1


M, N = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append([i, j])

print(bfs(i, j))
