'''
https://www.acmicpc.net/problem/1676
'''

# 제출 답안
import sys
def factorial(n,r):
    if n<1:
        return 1
    return n*factorial(n-1,n*r)

N = factorial(int(sys.stdin.readline()),1)
N = list(str(N)[::-1])
for i in range(len(N)):
    if N[i]!='0':
        print(i)
        break
