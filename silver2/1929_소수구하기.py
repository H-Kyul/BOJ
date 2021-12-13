# 에라토스테네스의 체

# 제출 답안
import math
import sys

M,N = map(int,sys.stdin.readline().split())
sosu = [0,0] + [i for i in range(2,N+1)]
for i in range(2,N+1):
    if sosu[i] != 0:
        for j in range(i+i,N+1,i):
            sosu[j] = 0
sosu = [i for i in sosu[M:] if sosu[i] != 0]
print(*sosu,sep='\n')
