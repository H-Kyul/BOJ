# https://www.acmicpc.net/problem/10773

import sys
N = int(sys.stdin.readline())
s = []
for _ in range(N):
    data = int(sys.stdin.readline())
    if data != 0:
        s.append(data)
    else:
        s.pop()
if len(s) == 0:
    print("0")
else:
    print(sum(s))
