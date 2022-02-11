'''
https://www.acmicpc.net/problem/11724
'''

# 제출 답안

import sys
from collections import deque
def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        for x in graph[v]:
            if visited[x] == 0:
                visited[x] = 1
                q.append(x)
                

n,m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1,n+1):
    if graph[i] == []:
        cnt+=1
        continue
    for j in graph[i]:
        if visited[j] == 0:
            bfs(j)
            cnt+=1
print(cnt)
