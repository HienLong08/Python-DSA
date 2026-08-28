with open("AddDigits.INP", "r") as fin:
    data = fin.readlines()
    num = int(data[0])

while num >= 10:
    num = sum(int(i) for i in str(num))

with open("AddDigits.OUT", "w") as fout:
    fout.writelines(str(num))

print(num)