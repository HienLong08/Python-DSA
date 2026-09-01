with open("Lemonade Change.INP", "r") as fin:
    data = fin.readlines()
    bills = list(map(int, data[0].split()))

five = 0
ten = 0
Result = True

for i in range(len(bills)):
    if bills[i] == 5:
        five += 1

    if bills[i] == 10:
        if five >= 1:
            five -= 1
            ten += 1
        else:
            Result = False
            break

    if bills[i] == 20:
        if ten >= 1 and five >= 1:
            ten -= 1
            five -= 1
        elif five >= 3:
            five -= 3
        else:
            Result = False
            break

with open("Lemonade Change.OUT", "w") as fout:
    fout.write(Result)
            
    