import sys
N = int(input())
nums = list(sys.stdin.readline().split() for _ in range(N)) # 1
nums = [[int(a),int(b)] for a,b in nums] # 2
nums = sorted(nums, key = lambda x: [x[0],x[1]]) # 3
for a,b in nums:
    print(a,b)
    
    
# 리스트 생성을 세 단계를 거침.
# -1 ) N개만큼 입력 받기 > 결과 문자열로 입력됨
# -2 ) 각 요소 정수형으로 변경
# -3 ) X값, Y값 기준 정렬

# 더 간단하게 리스트 생성할 방법은?
