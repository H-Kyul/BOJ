# 제출 답안

import sys
T = int(sys.stdin.readline())

for _ in range(T):
    case = list(sys.stdin.readline().strip())
    temp = []
    for c in case:
        temp.append(c)
        for i in range(len(temp)-1):
            if (temp[i] == '(') & (temp[i+1] == ')'):
                del temp[i:i+2]
                break

    if temp:
        print("NO")
    else:
        print("YES")

