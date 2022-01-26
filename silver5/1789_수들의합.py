'''
https://www.acmicpc.net/problem/1789
'''

# 제출 답안 2 - 이분탐색/1부터 n까지의 합 공식 이용
import sys
n = int(sys.stdin.readline())
s,e = 0,n
while s<=e:
    mid = (s+e)//2
    nSum = mid * (mid + 1) // 2
    if nSum > n:
        e = mid-1
    else:
        s = mid+1
print(e)

# 제출 답안 1
import sys
n = int(sys.stdin.readline())
hap=0
cnt=0
for i in range(1,n+1):
    hap+=i
    cnt+=1
    if hap > n:
        break
print(cnt-1)
