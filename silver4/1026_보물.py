'''
https://www.acmicpc.net/problem/1026
'''

# 제출 답안
import sys
N = int(sys.stdin.readline())
A = sorted(map(int,sys.stdin.readline().split()))
B = sorted(map(int,sys.stdin.readline().split()),reverse=True)
S = [x*y for x,y in zip(A,B)]
print(sum(S))
