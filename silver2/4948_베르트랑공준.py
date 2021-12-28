'''
https://www.acmicpc.net/problem/4948

시간을 단축시킬 방법 ??
'''

# 제출 답안
import sys

def sosu(n):
    import math
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

inputs = []
while True:
    n = int(sys.stdin.readline())
    if n==0:
        break
    inputs.append(n)
sosu_chk = [0 for _ in range(2*max(inputs)+1)]
for i in range(1,2*max(inputs)+1):
    if sosu(i):
        sosu_chk[i] = 1
for num in inputs:
    print(sum(sosu_chk[num+1:2*num+1]))
