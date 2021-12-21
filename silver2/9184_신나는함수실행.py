# 제출 답안

import sys
MAX = 21
res = [[[0]*MAX for _ in range(MAX)] for _ in range(MAX)]

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a >= MAX or b >= MAX or c >= MAX:
        return w(20,20,20)
    # 이미 저장된 값이면
    if res[a][b][c]:
        return res[a][b][c]

    # 그외 조건
    if a < b < c:
        res[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        res[a][b][c] =  w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return res[a][b][c]

while True:
    a,b,c = map(int,sys.stdin.readline().split())
    if a == b == c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
