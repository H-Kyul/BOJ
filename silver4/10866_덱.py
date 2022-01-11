'''
https://www.acmicpc.net/problem/10866
'''

# 제출 답안
import sys
from collections import deque
q = deque()
N = int(sys.stdin.readline())
for _ in range(N):
    s  = sys.stdin.readline().split()
    if "h_f" in s[0]: q.appendleft(s[1])
    if "h_b" in s[0]: q.append(s[1])
    if "p_f" in s[0]: print(q.popleft()) if q else print(-1)
    if "p_b" in s[0]: print(q.pop()) if q else print(-1)
    if "size" in s: print(len(q))
    if "empty" in s: print(0) if q else print(1)
    if "front" in s: print(q[0]) if q else print(-1)
    if "back" in s: print(q[-1]) if q else print(-1)
