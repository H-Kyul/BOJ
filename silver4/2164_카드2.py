'''
https://www.acmicpc.net/problem/2164
'''

# 제출 답안
from collections import deque
N = int(input())
q = deque(list(range(1,N+1)))
while len(q)!=1:
    q.popleft()
    q.append(q.popleft())
print(q[0])
