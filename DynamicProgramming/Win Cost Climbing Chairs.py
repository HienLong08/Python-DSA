with open("Win Cost Climbing Chairs.INP", "r") as fin:
    data = fin.readlines()
    cost = list(map(int, data[0].split()))

Ds = [0] * len(cost)

Ds[0] = cost[0]
Ds[1] = cost[1]

for i in range(2, len(cost)):
    Ds[i] = cost[i] + min(Ds[i - 1], Ds[i - 2])

answer = min(Ds[-1], Ds[-2])

with open("Win Cost Climbing Chairs.OUT", "w") as fout:
    fout.write(str(answer))
    