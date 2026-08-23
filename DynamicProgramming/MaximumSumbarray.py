# Maximum Subarray - Dynamic Programming (Kadane's Algorithm)
# Given an integer array nums, find the contiguous subarray with the largest sum.
# Return the largest sum.
# Example:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: The subarray [4, -1, 2, 1] has the largest sum of 6.

with open("MaximumSumbarray.INP", "r") as fin:
    data = fin.readlines()
    nums = list(map(int, data[0].split()))

Ds = [0] * len(nums)
Ds[0] = nums[0]

for i in range(1, nums):
    Ds[i] = max(Ds[i - 1] + nums[i], num[i])
    
with open("MaximumSumbarray.OUT", "w") as fout:
    with open(str(max(Ds)))
    
print(max(Ds))