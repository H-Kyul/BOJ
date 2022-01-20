

# 제출 답안 - 실패

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
            out = time.popleft()
            del(candidates[out])
            time.append(x)
            candidates[x] = 1
        else:
            time.append(x)
            candidates[x] = 1

print(*sorted(map(int,candidates.keys())))
