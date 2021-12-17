# N,M 입력
M,N = map(int,sys.stdin.readline().split())
print(M,N)
# 지도입력
graph = [list(map(int,sys.stdin.readline().split())) for _ in range (N)]
print(graph)
