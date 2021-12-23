'''

'''

# 제출 답안

import sys
N = int(sys.stdin.readline())
tempN = N
cnt = 0
while True:
    sum = tempN//10 + tempN%10
    tempN = (tempN%10)*10 + sum%10
    cnt+=1
    if tempN == N:
        break

print(cnt)
