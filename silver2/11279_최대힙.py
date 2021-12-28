'''
https://www.acmicpc.net/problem/11279
'''

# 제출 답안
import sys
import heapq
N = int(sys.stdin.readline())
inputs = [int(sys.stdin.readline()) for _ in range(N)]
heap = []

for num in inputs:
    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,(-num,num))
