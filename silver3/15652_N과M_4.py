# 제출답안 - 중복조합은 combinations_with_replacement()
from itertools import combinations_with_replacement
import sys

N,M = sys.stdin.readline().split()
numbers = list(range(1,int(N)+1))
for p in combinations_with_replacement(numbers,int(M)):
    print(*p,sep=' ')

    
    
'''
# 문제정의
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.

# 출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력
'''
