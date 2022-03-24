'''
https://www.acmicpc.net/problem/1018
'''

# 제출 답안 2
import sys
input = sys.stdin.readline
m,n = map(int,input().split())
matrix = [list(input()) for _ in range(m)]
matrix = [[1 if matrix[i][j]=='B' else 0 for j in range (n)] for i in range (m)]

def board(x,y):
    w_corner,b_corner = 0,0
    check = 0
    for i in range(x,x+8):
        check += sum(matrix[i][y:y+8])
    if check%64 == 0:
        return 32
    for i in range(x,x+8):
        for j in range(y,y+8):

            if matrix[i][j]:
                if (i+j)%2: 
                    b_corner +=1  
                else:
                    w_corner +=1 
            else:
                if (i+j)%2:
                    w_corner += 1  
                else:
                    b_corner += 1  
    return min(b_corner,w_corner)


change = 32
for i in range(m-7):
    for j in range(n-7):
        change = min(change,board(i,j))
print(change)

# 제출 답안 1

import sys
input = sys.stdin.readline
m,n = map(int,input().split())
matrix = [list(input()) for _ in range(m)]
matrix = [[1 if matrix[i][j]=='B' else 0 for j in range (n)] for i in range (m)]

def board(x,y):
    arr = []
    w_check,b_check = 0,0
    check = 0
    for i in range(x,x+8):
        check += sum(matrix[i][y:y+8])
    if check == 0 or check == 64:
        return 32
    for i in range(x,x + 8):
        arr.append(matrix[i][y:y+8])
        org = matrix[i][y:y + 8]
        w_corner = [0,1]*4
        b_corner = [1,0]*4
        if i%2 == 1:
            w_corner = [1,0]*4
            b_corner = [0,1]*4
        w_check += sum([1 for a,b in zip(org,w_corner) if a!=b])
        b_check += sum([1 for a,b in zip(org,b_corner) if a!=b])

    return min(w_check,b_check)

change = 32
for i in range(m-7):
    for j in range(n-7):
        change = min(change,board(i,j))
print(change)
