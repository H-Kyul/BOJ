'''
https://www.acmicpc.net/problem/1927
'''

# 제출 답안

import sys
import heapq

N = int(sys.stdin.readline())
inputs = [int(sys.stdin.readline()) for _ in range(N)]
heap = []
for x in inputs:
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,x)
