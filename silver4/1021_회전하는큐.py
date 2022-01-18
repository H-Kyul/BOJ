'''
https://www.acmicpc.net/problem/1021
'''

# 제출 답안
from collections import deque
N,M = map(int,input().split())
q= deque(list(range(1,N+1)))
targets = list(map(int,input().split()))

cnt = 0
for i in targets:
    idx = q.index(i)
    q_len = len(q)
    while True:
        if idx == 0:
            q.popleft()
            break
        if idx <= q_len-idx:
            q.append(q.popleft())
            cnt+=1; idx-=1
        else:
            q.appendleft(q.pop())
            cnt+=1; idx+=1
        if idx < 0: idx = q_len
        if idx >= q_len: idx = 0

print(cnt)
