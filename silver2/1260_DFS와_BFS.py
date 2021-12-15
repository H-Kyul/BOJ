'''
# 문제 정의
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
'''


# 제출 답안
import sys
from collections import deque

def dfs(v):
    visited[v] = True
    print(v, end= ' ')
    for x in Graph[v]:
        if visited[x] == False:
            dfs(x)

def bfs(v,queue):
    b_visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for x in Graph[v]:
            if b_visited[x] == False:
                b_visited[x] = True
                queue.append(x)


# 공통 - 그래프 생성
N,M,V = map(int,sys.stdin.readline().split())

Graph = [[] for _ in range(N+1)]
for i in range (M):
    V1,V2 = map(int,sys.stdin.readline().split())
    Graph[V1].append(V2)
    Graph[V2].append(V1)

for edge in Graph:
    edge.sort()

# DFS
visited = [False]*(N+1)
dfs(V)

print()
# BFS
queue = deque([V])
b_visited = [False]*(N+1)
bfs(V,queue)
