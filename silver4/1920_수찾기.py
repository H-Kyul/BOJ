'''
https://www.acmicpc.net/problem/1920

# 문제 정의
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.


'''

# 제출 답안 2 - bisect 모듈
from bisect import bisect_left,bisect_right
N = int(input())
arr = sorted(map(int,input().split()))
M = int(input())
target = list(map(int,input().split()))

for data in target:
    r = bisect_right(arr,data)
    l = bisect_left(arr,data)
    if l < r:
        print(1)
    else:
        print(0)
        
        
        
# 제출 답안 1
import sys
def binarysearch(arr,target):
    s = 0
    e = len(arr)-1
    while s <= e:
        mid = (s+e)//2
        if arr[mid] == target:
            return 1
        if arr[mid] > target:
            e = mid-1
        else:
            s = mid+1
    return 0

N = int(sys.stdin.readline())
L1 = sorted(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
L2 = list(map(int,sys.stdin.readline().split()))

for data in L2:
    print(binarysearch(L1,data))
