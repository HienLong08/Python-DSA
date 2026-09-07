with open("House Robber.INP", "r") as fin:
    data = fin.readlines()
    nums = list(map(int, data[0].split()))
    
Dp = [0] * len(nums)
    
with open("House Robber.OUT", "w") as fout:
    if len(nums) >= 2:
        Dp[0] = nums[0]
        Dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            Dp[i] = max(Dp[i - 1], Dp[i - 2] + nums[i])
        fout.writelines(str(max(Dp)))
    else:
        fout.writelines(str(nums[0]))