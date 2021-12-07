# 답안 1 - sorted 내장함수
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
for num in sorted(nums):
    print(num)

    
    
# 답안 2
N = int(input())
nums = list(int(input()) for _ in range(N))
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] > nums[j]:
            nums[i],nums[j] = nums[j],nums[i]
for num in sorted(nums):
    print(num)
