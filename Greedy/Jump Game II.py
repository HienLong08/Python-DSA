with open("Jump Game II.INP", "r") as fin:
    data = fin.readlines()
    nums = list(map(int, data[0].split()))

Dem = 1
Start = 1
End = nums[0]
Max = 0
MaxPos = 0

while End < len(nums) - 1:
    Max = 0
    for i in range(Start, End + 1):
        if nums[i] + i > Max:
            Max = nums[i] + i
            MaxPos = i
    Dem += 1
    Start = End + 1
    End = MaxPos + nums[MaxPos]
    
with open("Jump Game II.OUT", "w") as fout:
    if len(nums) == 1:
        fout.write("0")
    else:
        fout.write(str(Dem))
