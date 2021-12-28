'''
https://www.acmicpc.net/problem/9461
'''

# 제출 답안

arr = [1,1,1,2,2,3,4,5,7,9]
case = [int(input()) for _ in range(int(input()))]
if max(case) > len(arr):
    for i in range(10,max(case)):
        arr.append(arr[i-5]+arr[i-1])
for i in case:
    print(arr[i-1])
