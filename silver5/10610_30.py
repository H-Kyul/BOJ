'''
https://www.acmicpc.net/problem/10610
'''

# 제출 답안
import sys
n = sorted(map(int,sys.stdin.readline().strip()),reverse=True)
hap = sum(n)
if hap%3==0 and n[-1]==0:
      print("".join(map(str,n)))
else:
      print(-1)
