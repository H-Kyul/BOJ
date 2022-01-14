'''
https://www.acmicpc.net/problem/11659
'''

# 제출 답안
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
nums = list(map(int,input().split()))
for i in range(1,N):
    nums[i] += nums[i-1]
for _ in range(M):
    i,j = map(int,input().split())
    if i==1:
        print(nums[j-1])
    else:
        print(nums[j-1]-nums[i-2])
