'''
https://www.acmicpc.net/problem/1065
'''


# 제출 답안 2 - 리스트 활용
import sys

n = int(sys.stdin.readline())
cnt = 0
for i in range(1,n+1):
    num = list(map(int, str(i)))
    if i<100 or num[0]-num[1]==num[1]-num[2]:
        cnt+=1
print(cnt)



# 제출 답안 1 
import sys

n = int(sys.stdin.readline())
cnt = 0
for i in range(1,n+1):
    if i<100:
        cnt+=1
    else:
        a,b,c = i//100,i%100//10,i%10
        if a-b==b-c:
            cnt+=1
print(cnt)
