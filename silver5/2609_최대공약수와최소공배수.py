'''
https://www.acmicpc.net/problem/2609
'''

# 제출 답안 2
import sys
input = sys.stdin.readline
def GCD(a,b):
    for i in range(min(a,b),1,-1):
        if a % i == 0 and b % i == 0:
            return i
    return 1
a,b = map(int,input().split())
gcd = GCD(a,b)
print(gcd, a*b//gcd,sep='\n')


# 제출 답안 1 - math 이용

import sys
import math
input = sys.stdin.readline

a,b = map(int,input().split())
gcd = math.gcd(a,b)
print(gcd, a*b//gcd,sep='\n')


