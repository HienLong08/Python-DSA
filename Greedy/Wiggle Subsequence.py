with open("Wiggle Subsequence.INP", "r") as fin:
    data = fin.readlines()
    nums = list(map(int, data[0].split()))
    
Dem = 1
up = True
Start = nums[0]
Index = 0

for i in range(1, len(nums)):
    if nums[i] < Start:
        up = False
        Start = nums[i]
        Index = i
        Dem += 1
        break
    if nums[i] > Start:
        up = True
        Start = nums[i]
        Index = i
        Dem += 1
        break
        
for i in range(Index, len(nums)):
    if not up:
        if nums[i] > Start:
            Start = nums[i]
            Dem += 1
            up = True
        else:
            Start = nums[i]
    if up:
        if nums[i] < Start:
            Start = nums[i]
            Dem += 1
            up = False
        else:
            Start = nums[i]
            
with open("Wiggle Subsequence.OUT", "w") as fout:
    fout.writelines(str(Dem))
    