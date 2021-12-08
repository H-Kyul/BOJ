from collections import Counter
import sys

N = int(input())
nums = sorted(int(sys.stdin.readline()) for _ in range(N))
print(round(sum(nums)/N))  # 산술평균
print(nums[N // 2])  # 중앙값
# 최빈값
freq = Counter(nums).most_common()
if len(freq) == 1:
    print(freq[0][0])
else:
    print(freq[0][0]) if (freq[0][1] != freq[1][1]) else print(freq[1][0])
print(nums[-1] - nums[0])  # 범위
