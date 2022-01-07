'''
https://www.acmicpc.net/problem/2178
'''

# 제출 답안
import sys
def bfs(i,j):
    from collections import deque
    visited[i][j] = 1
    q = deque([[i,j]])
    while q:
        x,y = q.popleft()
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if (maze[nx][ny] == 1) and (visited[nx][ny] == 0):
                    q.append([nx,ny])
                    visited[nx][ny] += visited[x][y] +1

N,M = map(int, sys.stdin.readline().split())
maze = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

bfs(0,0)
print(visited[N-1][M-1])
