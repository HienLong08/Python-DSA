with open("CanPlaceFlower.INP", "r") as fin:
    data = fin.readlines()
    flowered = list(map(int, data[0].split()))
    n = int(data[1])

Dem = 0

if flowered[0] == 0 and flowered[1] == 0:
    flowered[0] = 1
    Dem += 1

for i in range(1, len(flowered) - 1):
    if flowered[i - 1] == 0 and flowered[i] == 0 and flowered[i + 1] == 0:
        flowered[i] = 1
        Dem += 1

if flowered[-1] == 0 and flowered[-2] == 0:
    flowered[-1] = 1
    Dem += 1

with open("CanPlaceFlower.OUT", "w") as fout:
    if Dem >= n:
        fout.writelines("true")
    else:
        fout.writelines("false")
    