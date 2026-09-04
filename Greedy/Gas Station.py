with open("Gas Station.INP", "r") as fin:
    data = fin.readlines()
    gas = list(map(int, data[0].split()))
    cost = list(map(int, data[1].split()))

Start = 0
tank = 0

with open("Gas Station.OUT", "w") as fout:
    if sum(gas) < sum(cost):
        fout.write("-1")
    else:
        for i in range(len(cost)):
            tank += gas[i] - cost[i]

            if tank < 0:
                Start = i + 1
                tank = 0

        fout.write(str(Start))