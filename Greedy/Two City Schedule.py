with open("Two City Schedule.INP", "r") as fin:
    data = fin.readlines()
    n = int(data[0])
    costs = list(map(int, data[1].split()))

Ds = []
Cost = 0
    
for i in range(1, n + 1):
    cost = list(map(int, data[i].split()))
    Ds.append(cost)
    
Ds.sort(key=lambda x: x[1] - x[0])

for i in range(n):
    Cost += Ds[i][0]

for i in range(n, 2 * n):
    Cost += Ds[i][1]

with open("Two City Schedule.OUT", "w") as fout:
    fout.writelines(str(Cost))

    