'''
https://www.acmicpc.net/problem/2559
'''

# 제출 답안

import sys
n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
ans = [sum(arr[:k])]
for i in range(n-k):
    ans.append(ans[-1]-arr[i]+arr[i+k])
print(max(ans))

