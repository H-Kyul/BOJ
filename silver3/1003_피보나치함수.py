
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
