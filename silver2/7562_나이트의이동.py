'''
https://www.acmicpc.net/problem/7562
'''

# 제출 답안 2 - 함수로 변경: 시간&메모리 단축(3996ms > 2568ms)
import sys
from collections import deque
input = sys.stdin.readline
def bfs(sx,sy,fx,fy):
    q = deque([[sx, sy]])
    while q:
        x, y = q.popleft()
        if x == fx and y == fy:
            return visited[x][y]
        dx = [-1, -2, -2, -1, 1, 2, 2, 1]
        dy = [-2, -1, 1, 2, -2, -1, 1, 2]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

for _ in range(int(input())):
    l = int(input())
    visited = [[0]*l for _ in range(l)]
    sx,sy = map(int,input().split())
    fx,fy = map(int,input().split())
    print(bfs(sx,sy,fx,fy))
    
# 제출 답안 1 

import sys
from collections import deque
input = sys.stdin.readline
for _ in range(int(input())):
    l = int(input())
    visited = [[0]*l for _ in range(l)]
    sx,sy = map(int,input().split())
    fx,fy = map(int,input().split())
    q = deque([[sx,sy]])
    while q:
        x,y = q.popleft()
        if x==fx and y==fy:
            print(visited[x][y])
            break
        dx = [-1,-2,-2,-1,1,2,2,1]
        dy = [-2,-1,1,2,-2,-1,1,2]
        for i in range(8):
            nx =  x + dx[i]
            ny =  y + dy[i]
            if 0 <= nx < l and 0<= ny < l and visited[nx][ny]==0:
                q.append([nx,ny])
                visited[nx][ny] = visited[x][y]+1
