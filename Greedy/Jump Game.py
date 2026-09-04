with open("Jump Game.INP", "r") as fin:
    data = fin.readlines()
    nums = list(map(int, data[0].split()))

Max = 0
result = False

for i in range(len(nums)):
    if i > Max:
        break

    Max = max(Max, i + nums[i])
    if Max >= len(nums) - 1:
        result = True
        break

with open("Jump Game.OUT", "w") as fout:
    fout.write(str(result))