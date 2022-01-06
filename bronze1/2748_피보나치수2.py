'''
https://www.acmicpc.net/problem/2748
'''

# 제출 답안
import sys
N = int(sys.stdin.readline())
fibo = [0,1]

for i in range (2,N+1):
    fibo.append(fibo[i-2]+fibo[i-1])
print(fibo[N])
