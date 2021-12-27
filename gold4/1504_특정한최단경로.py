'''
https://www.acmicpc.net/problem/1504
'''

# 제출 답안

import heapq
import sys

input = sys.stdin.readline
INF = float('INF')

# 정점, 간선 개수
N,E = map(int,input().split())

# 그래프
graph = [[] for _ in range(N+1)]
for i in range(E):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])


# 통과 조건
v1,v2 = map(int,input().split())

# 다익스트라
def dijkstra(start,end):
    q = []
    costs = [INF] * (N + 1)
    costs[start] = 0
    heapq.heappush(q,(costs[start],start)) # (비용,노드)
    
    while q:
        dist, node = heapq.heappop(q)
        if costs[node] < dist:
            continue

        for edge in graph[node]:
            cost = dist + edge[1]
            if cost < costs[edge[0]]:
                costs[edge[0]] = cost
                heapq.heappush(q,(cost, edge[0]))
    return costs[end]

# 조건을 만족하는 경로 탐색
res1 = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,N)
res2 = dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,N)

print(min(res1,res2)) if min(res1,res2) < INF else  print(-1)
