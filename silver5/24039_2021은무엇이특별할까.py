'''
https://www.acmicpc.net/problem/24039
'''

# 제출 답안
import sys
from math import sqrt
def sosu(n):

    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

n = int(sys.stdin.readline())
arr = []
for i in range(2,10000):
    if sosu(i):
        arr.append(i)
    if len(arr) >= 2:
        special = arr[-1] * arr[-2]
        if special > n:
            print(special)
            break
