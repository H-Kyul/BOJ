'''
https://www.acmicpc.net/problem/2630
'''

# 제출 답안

import sys
def divide(x,y,size):
    global w,b
    oneColor = 0
    check = sum([arr[i][j] for i in range(x,x+size) for j in range(y,y+size)])

    if check ==0 or check == size**2:
        oneColor = 1

    if oneColor == 1:
        if arr[x][y] == 0:
            w+=1
        else:
            b+=1
        return

    size //= 2
    divide(x, y, size)
    divide(x, y + size, size)
    divide(x + size, y, size)
    divide(x + size, y + size, size)

n = int(sys.stdin.readline())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
w,b = 0,0
divide(0,0,n)
print(w,b)
