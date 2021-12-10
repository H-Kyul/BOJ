import sys
from collections import deque
N = int(sys.stdin.readline())
# orders = list(sys.stdin.readline().split() for _ in range(N))
q = deque()
for i in range(N):
    o = sys.stdin.readline().split()
    if o[0] == 'push':
        q.append(int(o[1]))
    elif o[0] == 'pop':
        try:
            print(q.popleft())
        except:
            print(-1)
    elif o[0] == 'size':
        print(len(q))
    elif o[0] == 'empty':
        print(0 if q else 1)
    elif o[0] == 'front':
        try:
            print(q[0])
        except:
            print(-1)
    elif o[0] == 'back':
        try:
            print(q[-1])
        except:
            print(-1)
