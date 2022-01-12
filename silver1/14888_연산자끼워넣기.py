'''
https://www.acmicpc.net/problem/14888
'''

# 제출 답안
import sys
from itertools import permutations
def calculate(N, A, operator):
    res = A[0]

    for i in range(N - 1):
        if operator[i] == '+':
            res += A[i + 1]
        elif operator[i] == '-':
            res -= A[i + 1]
        elif operator[i] == '*':
            res *= A[i + 1]
        elif operator[i] == '/':
            res = int(res / A[i + 1])
        if res > 10**9 or res < -10**9:
            res = None
            break
    return res

MAX,MIN= -10**9, 10**9
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
opNums = list(map(int,sys.stdin.readline().split()))
operator = ['+','-','*','/']
opList = []
for i in range(4):
    opList += opNums[i] * operator[i]

operators = set(permutations(opList))   
for op in operators:
    res = calculate(N, A, op)
    if res < MIN:
        MIN = res
    if res > MAX:
        MAX = res

print(MAX)
print(MIN)
