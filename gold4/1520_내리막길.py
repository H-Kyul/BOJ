'''
https://www.acmicpc.net/problem/1520
'''

# 제출 답안

import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1

    if dp[x][y] != -1: # 이미 지나친 길이면, 저장된 정보 활용
        return dp[x][y]
      
    dp[x][y]= 0
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx = x + dx;
        ny = y + dy
        if (0 <= nx < m) and (0 <= ny < n) and map[nx][ny] < map[x][y]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]


m, n = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]
print(dfs(0, 0))
