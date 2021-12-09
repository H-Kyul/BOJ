'''
# 문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오

https://www.acmicpc.net/problem/10989
'''


# 제출 답안
import sys
N = int(sys.stdin.readline())
cnt = [0 for _ in range(10001)]
for _ in range(N):
    num = int(sys.stdin.readline())
    cnt[num] += 1
nums = [[n,c] for n,c in enumerate(cnt)]
for n,c in nums:
    for _ in range (c):
        print(n)
        
        
'''
9번의 시도 후(메모리초과) 문제 해결
- 주어지는 수는 10,000보다 작거나 같은 자연수(주어지는 "개수"가 아님)
- 문제: 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력 >> 기존 : 정렬 결과를 리스트로 생성한 후 출력 > 변경 : 바로 출력
'''
