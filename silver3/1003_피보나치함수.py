# 제출 답안 

import sys
N = int(sys.stdin.readline())
cases = list(int(sys.stdin.readline()) for _ in range(N))
fibo = [[1,0],[0,1]] + [[0,0] for _ in range (max(cases)-1)]
for i in range(2,max(cases)+1):
    fibo[i] = [x+y for x,y in zip(fibo[i-2],fibo[i-1])]
for case in cases:
    print(*fibo[case],sep=' ')
    
    
# 실패 - 시간초과(16%까지 채점) 
import sys
def fibonacci(N,cnt):
    if N == 0:
        cnt[0]+= 1
        return N,cnt
    elif N == 1:
        cnt[1] += 1
        return N,cnt
    else:
        return fibonacci(N-1,cnt) + fibonacci(N-2,cnt),cnt

N = int(sys.stdin.readline())
Cases = list(int(sys.stdin.readline()) for _ in range(N))

for case in Cases:
    cnt = [0] * 2
    result,cnt = fibonacci(case,cnt)
    print(*cnt,sep=' ')
