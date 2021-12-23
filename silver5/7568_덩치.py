'''
https://www.acmicpc.net/problem/7568
'''

# 제출 답안
import sys

N = int(sys.stdin.readline())
p = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
rank = []
for a,b in p:
    cnt = 1
    for c,d in p:
        if (a<c)&(b<d):
            cnt+=1
    rank.append(cnt)
print(*rank)
