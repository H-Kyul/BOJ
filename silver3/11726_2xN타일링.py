'''
https://www.acmicpc.net/problem/11726
'''

# 제출 답안 2
import sys
n = int(sys.stdin.readline())
a,b = 1,1
for i in range(n):
    a,b = b,a+b
print(a%10007)

# 제출 답안 1
import sys
dp = [0,1,2]
n = int(sys.stdin.readline())
for i in range(3,n+1):
    dp.append(dp[i-2]+dp[i-1])
print(dp[n]%10007)
