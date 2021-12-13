'''
# 변경사항:
- 시간을 줄이고자 재시도
- 제곱근까지 반복 후, N!=1이라면, N 추가
- 시간단축 성공
  제출 1 : 메모리 29200KB	/ 시간 1120ms / 코드길이 95B
  제출 2 : 메모리 31312KB	/ 시간 68ms / 코드길이 307B
'''

# 제출 답안 2
import sys
import math
N = int(sys.stdin.readline())
ans = []
MAX = int(math.sqrt(N)) if N > 5 else N
for i in range(2,MAX+1):
    while N % i == 0:
        ans.append(i)
        N //= i
    if N == 1:
        break
    elif (i == MAX) & (N != 1):
        ans.append(N)
        N //= i

print(*ans,sep='\n')


# 제출 답안 1
N = int(input())
for i in range(2,N+1):
    while N % i == 0:
        print(i)
        N = N//i
