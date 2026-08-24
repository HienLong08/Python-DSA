with open("ClimbingStairs.INP", "r") as fin:
    data = fin.readlines()
    n = int(data[0])

if n <= 1:
    result = 1
else:
    Ds = [1] * n
    Ds[1] = 2

    for i in range(2, n):
        Ds[i] = Ds[i - 1] + Ds[i - 2]

    result = Ds[n - 1]

with open("ClimbingStairs.OUT", "w") as fout:
    fout.write(str(result))

print(result)