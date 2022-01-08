'''
https://www.acmicpc.net/problem/1271
'''

# 제출 답안
import sys
N,M = map(int,sys.stdin.readline().split())
print(N//M,N%M)
