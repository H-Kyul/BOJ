'''
https://www.acmicpc.net/problem/1085
'''

# 제출 답안
import sys

x,y,w,h = map(int,sys.stdin.readline().split())

print(min(abs(x-w),abs(y-h),x,y))
