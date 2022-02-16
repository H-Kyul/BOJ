'''
https://www.acmicpc.net/problem/1535
'''


# 제출 답안
import sys
input = sys.stdin.readline
def dp(hp,happy):
    d = [0]*100
    for p,h in zip(hp,happy):
        for k in range(p, 100)[::-1]:
            d[k] = max(d[k], d[k-p]+h)
    return d[99]

N = int(input())
hp = list(map(int,input().split()))
happy = list(map(int,input().split()))
print(dp(hp, happy))
