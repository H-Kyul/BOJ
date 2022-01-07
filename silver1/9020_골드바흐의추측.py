'''
https://www.acmicpc.net/problem/9020
'''

# 제출 답안
import math
import sys
def sosu(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    for i in range(N//2,1,-1):
        if sosu(i) & sosu(N-i):
            print(i,N-i)
            break
