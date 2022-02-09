'''
https://www.acmicpc.net/problem/1918
'''

# 제출 답안

import sys
prefix = list(sys.stdin.readline().strip())
ans = ''
s = []
for x in prefix:
    if x.isalpha():
        ans += x
    elif x == '(':
        s.append(x)
    elif x == ')':
        while s[-1] != '(':
            ans += s.pop()
        s.pop()
    elif x == '+' or x == '-':
        while s and s[-1] != '(':
            ans+=s.pop()
        s.append(x)
    elif x == '*' or x == '/':
        while s and (s[-1]== '*' or s[-1]=='/'):
            ans += s.pop()
        s.append(x)
while s:
    ans+=s.pop()
print(ans)
