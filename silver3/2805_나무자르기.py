'''
https://www.acmicpc.net/problem/2805
'''

# 제출 답안
import sys
def treeSum(x):
    return sum([x - MID for x in trees if x > MID])

N, M = map(int, sys.stdin.readline().split())
trees = sorted(map(int, sys.stdin.readline().split()))
MIN,MAX = 0,trees[-1]
while MIN <= MAX:
    MID = (MIN + MAX) // 2
    if treeSum(MID) >= M:
        MIN = MID +1
    else:
        MAX = MID - 1
print(MAX)
