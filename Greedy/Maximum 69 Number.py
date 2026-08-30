with open("Maximum 69 Number.INP", "r") as fin:
    data = fin.readlines()
    num = int(data[0])

Num = str(num)
i = 0
Ds = []

while i < len(Num):
    if Num[i] == "6":
        Ds.append("9")
        i += 1

        for j in range(i, len(Num)):
            Ds.append(Num[j])
        break

    else:
        Ds.append(Num[i])
        i += 1

with open("Maximum 69 Number.OUT", "w") as fout:
    fout.write("".join(Ds))
        