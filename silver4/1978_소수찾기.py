# 제출 답안
import sys
def sosu(x):
    import math
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

N = int(input())
L = list(map(int,sys.stdin.readline().split()))
cnt = 0

for x in L:
    if (x >= 2) & sosu(x):
        cnt +=1
print(cnt)
