'''
https://www.acmicpc.net/problem/2512
'''

# 제출 답안
import sys
input = sys.stdin.readline
N = int(input())
budgets = sorted(map(int,input().split()))
M = int(input())
l,r = 0,max(budgets)

while l<=r:
    mid = (l + r) // 2
    b_sum = sum([x if x<mid else mid for x in budgets ])
    if b_sum> M:
        r = mid -1
    else:
        l = mid +1
print(r)
