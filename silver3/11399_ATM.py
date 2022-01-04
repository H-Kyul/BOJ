'''
https://www.acmicpc.net/problem/11399
'''

# 제출 답안
import sys
N = int(sys.stdin.readline())
orders = sorted(map(int,sys.stdin.readline().split()))
for i in range(1,len(orders)):
    orders[i] += orders[i-1]
print(sum(orders))
