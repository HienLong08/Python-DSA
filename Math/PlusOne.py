with open("PlusOne.INP", "r") as fin:
    data = fin.readlines()
    digits = list(map(int, data[0].split()))

Ds = ""

for i in digits:
    Ds += str(i)

Num = int(Ds)
Num += 1
nums = str(Num)

List = list(map(int, nums))

with open("PlusOne.OUT", "w") as fout:
    fout.writelines(" ".join(str(x) for x in List))

