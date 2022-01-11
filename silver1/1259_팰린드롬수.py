'''
https://www.acmicpc.net/problem/1259
'''

# 제출 답안

import sys
while True:
    N = input()
    if N=='0':
        break
    if N==N[::-1]:
        print('yes')
    else:
        print('no')
