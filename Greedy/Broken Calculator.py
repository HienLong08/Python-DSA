with open("Broken Calculator.INP", "r") as fin:
    data = fin.readlines()
    StartValue = int(data[0])
    Target = int(data[1])

Dem = 0

while Target > StartValue:
    if Target % 2 == 0:
        Target //= 2
        Dem += 1
    else:
        Target += 1
        Dem += 1

with open("Broken Calculator.OUT", "w") as fout:
    fout.writelines(str(Dem + StartValue - Target))