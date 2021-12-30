'''
https://www.acmicpc.net/problem/10250
'''


# 제출 답안 2    --- 몫,나머지 규칙 이용
import sys
for _ in range(int(sys.stdin.readline())):
    H,W,N = map(int,sys.stdin.readline().split())
    hotel = [[0]*W for _ in range(H)]
    q,r = divmod(N,H)
    if r == 0:
        floor,num = H,q
    else:
        floor,num = r,q+1
    if num<10:
        num = '0' + str(num)
    print(int(str(floor)+str(num)))



# 제출 답안 1    --- 이중포문 이용
import sys
for _ in range(int(sys.stdin.readline())):
    H,W,N = map(int,sys.stdin.readline().split())
    hotel = [[0]*W for _ in range(H)]
    c = 0
    for i in range(W):
        for j in range(H):
            c+=1
            if c == N:
                if i<9:
                    ans = f'{j+1}0{i+1}'
                else:
                    ans = f'{j+1}{i+1}'
                print(int(ans))
                break

