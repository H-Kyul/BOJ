'''
https://www.acmicpc.net/problem/1934
https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95
'''

# 제출 답안 - 유클리안 호제법

import sys
def euclidean_gcd(a, b):
    if b == 0:
        return a
    else:
        a, b = b, a % b
        return euclidean_gcd(a, b)

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    if a < b: b, a = a, b
    print(a*b//euclidean_gcd(a, b))
