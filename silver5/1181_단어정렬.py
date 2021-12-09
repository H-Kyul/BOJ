'''
#문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력

'''

# 제출 답안
import sys
N = int(sys.stdin.readline())
Words = list(sys.stdin.readline().strip() for _ in range(N))
WD = dict([w,len(w)] for i,w in enumerate(Words))
WD = dict(sorted(WD.items(), key = lambda x:[x[1],x[0]]))
for w in WD.keys():
    print(w)
