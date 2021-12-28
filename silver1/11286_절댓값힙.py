'''
https://www.acmicpc.net/problem/11286
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
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,(abs(x),x))
        
# 절댓값 기준 정렬        
