# 제출 답안
import sys

N = int(sys.stdin.readline())
tile = [0]*(N+1)

for i in range(N+1):
    if i <= 2:
        tile[i] = i
    else:
        tile[i] = (tile[i-2]+tile[i-1])%15746
print(tile[N])
