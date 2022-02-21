'''
https://www.acmicpc.net/problem/11723
'''

# 제출 답안
import sys
m = int(sys.stdin.readline())
s = set()
for _ in range(m):
    order = sys.stdin.readline().split()
    od = order[0]
    if od == 'all':
        s = set(range(1,21))
    elif od == 'empty':
        s = set()
    else:
        x = int(order[1])
        if od == 'add' and x not in s:
            s.add(x)
        elif od == 'remove' and x in s:
            s.discard(x)
        elif od == 'check':
            print([0,1][x in s])
        elif od == 'toggle' and x in s:
            s.discard(x)
        elif od == 'toggle' and x not in s:
            s.add(x)
