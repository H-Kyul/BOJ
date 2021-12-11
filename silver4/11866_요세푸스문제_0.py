# 제출 답안

import sys
from collections import deque

N,K = map(int,sys.stdin.readline().split())
q = deque(range(1,N+1))
ans = '<'
cnt = 1
while q:
    if cnt < K:
        q.append(q.popleft())
        cnt += 1
    elif cnt == K:
        if len(q) == 1:
            ans += str(q.popleft()) + '>'
        else:
            ans += str(q.popleft()) + ', '
            cnt = 1
