'''
https://www.acmicpc.net/problem/1654

# 문제 정의
K개의 랜선으로 N개를 만들 수 있는 랜선의 최대 길이를 구하는 프로그램을 작성하시오.
'''

# 제출 답안
import sys
K,N = map(int,sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range (K)]
s = 1
e = sum(arr)//N

while s<=e:
    cnt = 0
    mid = (s+e)//2
    for line in arr:
        lan = line// mid
        cnt += lan
    if cnt >= N:
        s = mid +1
    else:
        e = mid -1

print(e)
