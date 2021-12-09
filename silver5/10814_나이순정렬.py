'''
# 문제
회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

https://www.acmicpc.net/problem/10814
'''


import sys
N = int(input())
p = list([i,sys.stdin.readline().split()] for i in enumerate(range(N)))
p = sorted(p, key = lambda x:int(x[1][0]))
for n in p:
    print(int(n[1][0]), n[1][1])
    
    
    
    
# 틀렸습니다 해결 > ['14','4'] 정렬 결과와 [14,4] 정렬 결과 비교
