'''
https://www.acmicpc.net/problem/1076
'''


# 제출 답안

import sys
ohm = dict([x,i] for i,x in enumerate(['ck','wn','ed','ge','ow','en','ue','et','ey','te']))
a,b,c = [sys.stdin.readline().strip()[-2:] for _ in range(3)]
v = (ohm[a]*10+ohm[b])*10**ohm[c]
print(v)


# 영문 전체 > 마지막 2글자로 변경(중복X)
