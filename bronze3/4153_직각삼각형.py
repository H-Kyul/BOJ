# 제출 답안
import sys

while True:
    A,B,C = sorted(map(int,sys.stdin.readline().split()))

    if C <=0 :
        break
    else:
        print(["wrong","right"][A**2+B**2 == C**2])
        
'''
# print 출력 부분 > 숏코딩 참고하여 수정

맞으면 "right", 틀리면 "wrong" 이므로
논리연산 True False을 활용
'''
