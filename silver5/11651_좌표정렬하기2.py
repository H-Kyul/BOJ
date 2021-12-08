import sys
N = int(input())
nums = list(sys.stdin.readline().split() for _ in range(N))
nums = [[int(a),int(b)] for a,b in nums]
nums = sorted(nums, key = lambda x: [x[1],x[0]])
for a,b in nums:
    print(a,b)
