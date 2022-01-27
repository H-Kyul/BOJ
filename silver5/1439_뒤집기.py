'''
https://www.acmicpc.net/problem/1439
'''

# 제출 답안
import sys
s = sys.stdin.readline().strip()
s_0 = [x for x in s.split('0') if x!='']
s_1 = [x for x in s.split('1') if x!='']
print(min(len(s_0),len(s_1)))
