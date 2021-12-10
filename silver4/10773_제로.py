'''
https://www.acmicpc.net/problem/10773

# 문제 정의
# 입력
첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)
이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

# 출력
재민이가 최종적으로 적어 낸 수의 합을 출력한다. 최종적으로 적어낸 수의 합은 231-1보다 작거나 같은 정수이다.
'''


import sys
N = int(sys.stdin.readline())
s = []
for _ in range(N):
    data = int(sys.stdin.readline())
    if data != 0:
        s.append(data)
    else:
        s.pop()
if len(s) == 0:
    print("0")
else:
    print(sum(s))
