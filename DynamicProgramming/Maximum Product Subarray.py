with open("Maximum Product Subarray.INP", "r") as fin:
    data = fin.readlines()
    nums = list(map(int, data[0].split()))
    
Max = [0] * len(nums)
Min = [0] * len(nums)

Max[0] = Min[0] = nums[0]

for i in range(1, len(nums)):
    Max[i] = max(Max[i - 1] * nums[i], Min[i - 1] * nums[i], nums[i])
    Min[i] = min(Min[i - 1] * nums[i], Max[i - 1] * nums[i], nums[i])
    
with open("Maximum Product Subarray.OUT", "w") as f:
    f.writelines(str(max(Max)))