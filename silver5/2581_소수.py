# 제출 답안
import sys
def sosu(x):
    import math
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

M = int(input())
N = int(input())
MinNum = -1
Sum = 0

for num in range(M,N+1):
    if (num >= 2) & sosu(num):
        Sum += num
        if MinNum == -1:
            MinNum = num

if Sum == 0:
    print(-1)
else:
    print(Sum,MinNum,sep='\n')
