'''
# 문제 정의
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
'''


# 제출 답안2 - BFS
import sys
from collections import deque

def BFS(v,queue):
    visited[v] = True
    while queue:
        v = queue.popleft()
        for x in Graph[v]:
            if visited[x] == False:
                visited[x] = True
                queue.append(x)
                
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

Graph = [[] for _ in range(N+1)]
for _ in range(M):
    V1,V2 = map(int,sys.stdin.readline().split())
    Graph[V1].append(V2)
    Graph[V2].append(V1)

visited = [False]*(N+1)
queue = deque([1])

BFS(1,queue)
print(visited.count(True)-1)


# 제출 답안1 - DFS
import sys
N = int(sys.stdin.readline()) 
M = int(sys.stdin.readline())

Graph = [[] for _ in range(N+1)]
for _ in range(M):
    V1,V2 = map(int,sys.stdin.readline().split())
    Graph[V1].append(V2)
    Graph[V2].append(V1)

visited = [False]*(N+1)
def DFS(v):
    visited[v] = True
    for x in Graph[v]:
        if visited[x] == False:
            DFS(x)
DFS(1)
print(visited.count(True)-1)
