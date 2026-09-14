with open("House Robber II.INP", "r") as fin:
    data = fin.readlines()
    nums = list(map(int, data[0].split()))
    
Ds = [0] * (len(nums) - 1)
DS = [0] * (len(nums) - 1)

Ds[0] = nums[0]
Ds[1] = max(nums[0], nums[1])
DS[0] = nums[1]
DS[1] = max(nums[1], nums[2])

for i in range(2, len(nums) - 1):
    Ds[i] = max(Ds[i - 2] + nums[i], Ds[i - 1])
    
for j in range(2, len(nums) - 1):
    DS[j] = max(DS[j - 2] + nums[j + 1], DS[j - 1])
    
with open("House Robber II.OUT", "w") as fout:
    if len(nums) == 1:
        fout.writelines(str(nums[0]))

    if len(nums) == 2:
        fout.writelines(str(max(nums[0], nums[1])))
        
    else:
        fout.writelines(str(max(max(DS), max(Ds))))
    

