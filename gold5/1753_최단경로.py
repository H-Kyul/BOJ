'''
https://www.acmicpc.net/problem/1753
'''

import heapq
import sys

input = sys.stdin.readline
INF = float('INF')

# 입력
V,E = map(int,input().split()) # 노드개수,간선개수
start = int(input())

# 그래프, 비용 정보 생성
costs = [INF]*(V+1)
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append([v,w])

# 다익스트라
def dijkstra(start):
    q = []
    costs[start] = 0 # 자기 자신과의 거리 0
    heapq.heappush(q,(costs[start],start)) # 힙에 (가중치,노드) 저장

    while q:
        dist, node = heapq.heappop(q)
        if costs[node] < dist:
            continue
        for edge in graph[node]:
            cost = dist + edge[1]
            if cost < costs[edge[0]]:
                costs[edge[0]] = cost
                heapq.heappush(q,(cost,edge[0]))

dijkstra(start)
# 최단 거리 출력
for i in range(1,V+1):
    print("INF") if costs[i] == INF else print(costs[i])
