'''
https://www.acmicpc.net/problem/1713
'''


# 제출 답안2 - 성공
import sys
input = sys.stdin.readline
N = int(input())
input()
data = list(input().split())
cand = dict()

for x in data:
    if x in cand:
        cand[x]+=1
        continue
    elif len(cand) == N:
        lowValue = min(cand.values())
        out = [k for k, v in cand.items() if v == lowValue][0]
        del (cand[out])

    cand[x] = 1
print(*sorted(map(int,cand.keys())))


# 제출 답안1 - 실패(틀렸습니다)

import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
data = list(input().split())
candidates = dict()
from collections import deque
time = deque([])

for x in data:
    if x in candidates:
        candidates[x] += 1
    else:
        if len(candidates) >= N:
            out = time.popleft() # <-------
            del(candidates[out])
            time.append(x)
            candidates[x] = 1
        else:
            time.append(x)
            candidates[x] = 1

print(*sorted(map(int,candidates.keys())))
