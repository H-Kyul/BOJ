'''
https://www.acmicpc.net/problem/2309
'''
# 리스트에서 삭제 후 출력 시 > 틀렸습니다

# 제출 답안
import sys
s = sorted([int(sys.stdin.readline()) for _ in range(9)])
for i in range(9):
    for j in range(1,9):
        if sum(s)-s[i]-s[j]==100:
            a,b = s[i],s[j]
            break
s = [x for x in s if x not in [a,b]]
print(*s,sep='\n')
