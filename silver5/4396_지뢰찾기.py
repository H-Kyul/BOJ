'''
https://www.acmicpc.net/problem/4396
'''

# 제출 답안 2 - 바로 출력, 지뢰 밟았는지 먼저 체크
n = int(input())
map = [list(input()) for _ in range(n)]
visited = [list(input()) for _ in range(n)]
bomb = 0

for i in range(n):
    for j in range(n):
        if visited[i][j]=='x' and map[i][j]=='*':
            bomb = 1
            break
for i in range(n):
    for j in range(n):
        cnt = 0
        if bomb and map[i][j] == '*':
            print('*',sep='',end='')
            continue
        if visited[i][j]=='.':
            print('.',sep='',end='')
            continue
        for x in range(i-1,i+2):
            for y in range(j-1,j+2):
                if 0<=x<n and 0<=y<n:
                    if map[x][y] == '*':
                        cnt += 1
        print(cnt,sep='',end='')
    print()


# 제출 답안
n = int(input())
map = [list(input()) for _ in range(n)]
visited = [list(input()) for _ in range(n)]# if input()=='x']
bomb = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        if visited[i][j]=='.':
            continue
        else:
            if map[i][j]=='*':
                bomb = 1
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    if 0<=x<n and 0<=y<n:
                        if map[x][y] == '*':
                            cnt += 1
            visited[i][j]=cnt

def Bomb(map,visited):
    for i in range(n):
        for j in range(n):
            if map[i][j]=='*':
                visited[i][j]='*'
    return visited

if bomb == 1:
    visited = Bomb(map,visited)
for i in visited:
    for line in i:
        print(line,sep='',end='')
    print()
