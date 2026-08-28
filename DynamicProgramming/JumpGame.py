with open("JumpGame.INP", "r") as fin:
    data = fin.readlines()
    nums = list(map(int, data[0].split()))

N = len(nums)

Ds = [False] * N
Ds[0] = True

for i in range(N):
    if Ds[i]:
        for j in range(1, nums[i] + 1):
            if i + j < N:
                Ds[i + j] = True

with open("JumpGame.OUT", "w") as fout:
    if Ds[N - 1]:
        fout.write("True")
    else:
        fout.write("False")