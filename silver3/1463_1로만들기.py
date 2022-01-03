'''
 https://www.acmicpc.net/problem/1463

# 틀렸습니다 해결 반례 : 29
https://www.acmicpc.net/board/view/6842
'''

import sys
N = int(sys.stdin.readline())
arr = [0] * (N+1)

for n in range(2,N+1):
    if n % 6 == 0:
        arr[n] = min(arr[n//2],arr[n//3])+1
    elif n % 2 == 0:
        arr[n] = min(arr[n-1],arr[n//2])+1
    elif n % 3 == 0:
        arr[n] = min(arr[n-1],arr[n//3])+1
    else:
        arr[n] = min(arr[n-1]+1,arr[n-2]+2)
print(arr[N])

