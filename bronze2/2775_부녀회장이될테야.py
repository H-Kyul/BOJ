'''
https://www.acmicpc.net/problem/2775
'''

# 제출 답안 2  -- 케이스 최대값까지 생성 후 출력
import sys
case = []
for _ in range(int(sys.stdin.readline())):
    case.append([int(sys.stdin.readline()) for _ in range(2)])

K = max(list(zip(*case))[0])
N = max(list(zip(*case))[1])
apt = [[]*N for _ in range(K+1)]
for i in range(K+1):
    for j in range(N):
        if i == 0:
            apt[i].append(j+1)
        else:
            apt[i].append(sum(apt[i-1][:j+1]))
for a,b in case:
    print(apt[a][b-1])



# 제출 답안 1   -- 케이스별로 확인

import sys
for _ in range(int(sys.stdin.readline())):
    K = int(sys.stdin.readline())
    N = int(sys.stdin.readline())

    apt = [[]*N for _ in range(K+1)]
    for i in range(K+1):
        for j in range(N):
            if i == 0:
                apt[i].append(j+1)
            else:
                apt[i].append(sum(apt[i-1][:j+1]))
    print(apt[K][N-1])

