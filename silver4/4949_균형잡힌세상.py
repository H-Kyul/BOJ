'''
https://www.acmicpc.net/problem/4949
'''

# 제출 답안

import sys

while True:
    case = list(sys.stdin.readline().rstrip()[:-1])
    if case == []:
        break

    temp = []
    for c in case:
        if c.isalpha() or c == " ":
            continue
        temp.append(c)

        for i in range(len(temp)-1):
            if ((temp[i] == '(') & (temp[i + 1] == ')'))\
                    or ((temp[i] == '[') & (temp[i + 1] == ']')):
                del temp[i:i + 2]
                break
    print(["yes","no"][bool(temp)])




