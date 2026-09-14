with open("Longest Increasing Subsequence.INP", "r") as fin:
    data = fin.readlines()
    nums = list(map(int, data[0].split()))
    
Dp = [1] * len(nums)

for i in range(1, len(nums)):
    for j in range(i):
        if nums[j] < nums[i]:
            Dp[i] = max(Dp[i], Dp[j] + 1)
        

KetQua = max(Dp)

with open("Longest Increasing Subsequence.OUT", "w") as fout:
    fout.write(str(KetQua))