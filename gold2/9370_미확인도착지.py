'''
https://www.acmicpc.net/problem/9370

특정 경로를 통과하는 예상 도착지 확인
'''


# 제출 답안
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(s):
    q = []
    distance = [INF]*(n+1)
    distance[s] = 0
    heapq.heappush(q,(0,s))

    while q:
        dist,node = heapq.heappop(q)
        if distance[node] < dist:
            continue

        for edge in graph[node]:
            cost = dist + edge[1]
            if cost < distance[edge[0]]:
                distance[edge[0]] = cost
                heapq.heappush(q,(cost,edge[0]))
    return distance

T = int(input())
for i in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range (m):
        a,b,d = map(int,input().split())
        graph[a].append([b,d])
        graph[b].append([a,d])

    ans = []
    from_s = dijkstra(s)
    from_g = dijkstra(g)
    from_h = dijkstra(h)
    for _ in range(t):
        x = int(input())
        direct = from_s[x]
        path = min(from_s[g] + from_g[h] + from_h[x],from_s[h] + from_h[g] + from_g[x])
        if path <= direct:
            ans.append(x)

    print(*sorted(ans))
