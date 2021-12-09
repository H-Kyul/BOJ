'''
# 문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
'''

# 제출 답안 2 - 힙
import sys
import heapq
N = int(sys.stdin.readline())
nums = list(int(sys.stdin.readline()) for _ in range(N))
heapq.heapify((nums))
while nums:
    print(heapq.heappop(nums))
    
    
# 제출 답안 1 - 내장함수 sorted
import sys
N = int(sys.stdin.readline())
nums = list(int(sys.stdin.readline()) for _ in range(N))
print(*sorted(nums),sep='\n')
