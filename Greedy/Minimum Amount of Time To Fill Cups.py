with open("Minimum Amount of Time To Fill Cups.INP", "r") as fin:
    data = fin.readlines()
    amount = list(map(int, data[0].split()))

amount.sort()
Second = 0

while amount[2] > 0:

    if amount[1] > 0:
        amount[1] -= 1
        amount[2] -= 1
        Second += 1

    else:
        Second += amount[2]
        break

    amount.sort()

with open("Minimum Amount of Time To Fill Cups.OUT", "w") as fout:
    fout.writelines(str(Second))
    
