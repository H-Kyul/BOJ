'''
https://www.acmicpc.net/problem/10816

상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
'''


# 제출 답안2 - Counter (시간단축 - 메모리 115032KB	/ 시간 920ms / 코드길이 294B)
from bisect import bisect_left,bisect_right
from collections import Counter
N = int(input())
arr = sorted(map(int,input().split()))
M = int(input())
target = list(map(int,input().split()))

counter = Counter(arr)
cnt = [counter.get(x) if x in counter else 0 for x in target]
print(*cnt,sep=' ')


# 제출 답안1 - bisect (메모리 114380KB	/ 시간 1664ms / 코드길이 342B)

from bisect import bisect_left,bisect_right
N = int(input())
arr = sorted(map(int,input().split()))
M = int(input())
target = list(map(int,input().split()))

cnt = [0 for _ in range(M)]
for i in range(len(target)):
    r = bisect_right(arr,target[i])
    l = bisect_left(arr,target[i])
    if l < r:
        cnt[i] += r-l

print(*cnt,sep=' ')
