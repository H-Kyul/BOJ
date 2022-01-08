'''
https://www.acmicpc.net/problem/1012
'''

# 제출 답안
import sys
sys.setrecursionlimit(10**6)
def dfs(x, y):
    visited[x][y] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < N) & (0 <= ny < M):
            if (graph[nx][ny] == 1) & (visited[nx][ny]==0):
                dfs(nx, ny)
for _ in range(int(sys.stdin.readline())):
    M,N,K = map(int,sys.stdin.readline().split())
    graph = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(K):
        x,y = map(int,sys.stdin.readline().split())
        graph[y][x] = 1
    for x in range(N):
        for y in range(M):
            if (graph[x][y]==1) & (visited[x][y]==0):
                dfs(x,y)
                cnt+=1

    print(cnt)
