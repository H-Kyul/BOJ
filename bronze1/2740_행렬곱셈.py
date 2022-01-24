'''
https://www.acmicpc.net/problem/2740
'''

# 제출 답안 2 - 시간 단축 500ms -> 168ms
# 아래 코드에서 2차원 리스트의 열부분만 추출하는 부분이 문제인 것으로 판단됨.
import sys
input = lambda:map(int,sys.stdin.readline().split())
N,M = input()
A = [list(input()) for _ in range(N)]
M,K = input()
B = [list(input()) for _ in range(M)]

for i in range(N):
    for j in range(K):
        print(sum([A[i][m] * B[m][j] for m in range(M)]),end=' ')
    print()


# 제출 답안 1 
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
M,K = map(int,input().split())
B = [list(map(int,input().split())) for _ in range(M)]
C = [[0]*K for _ in range(N)]
for i in range(N):
    for j in range(K):
        for a, b in zip(A[i], list(zip(*B))[j]):
            C[i][j] += a * b
for i in range(N):
    print(*C[i])
