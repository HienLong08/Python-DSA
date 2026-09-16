with open("Array Partition.INP", "r") as fin:
    data = fin.readlines()
    nums = list(map(int, data[0].split()))

nums.sort()

Dem = 0

for i in range(0, len(nums), 2):
    Dem += nums[i]

with open("Array Partition.OUT", "w") as fout:
    fout.write(str(Dem))