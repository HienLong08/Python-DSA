with open("Hand of Straight.INP", "r") as fin:
    data = fin.readlines()
    hand = list(map(int, data[0].split()))
    groupsize = int(data[1])

if len(hand) % groupsize != 0:
    KQ = "False"
else:
    hand.sort()
    Dictionary = {}

    for i in hand:
        if i not in Dictionary:
            Dictionary[i] = 1
        else:
            Dictionary[i] += 1

    KQ = "True"

    while True:
        Min = None

        for i in Dictionary:
            if Dictionary[i] > 0:
                Min = i
                break

        if Min is None:
            break

        Key = Dictionary[Min]

        for i in range(groupsize):
            if Min + i not in Dictionary:
                KQ = "False"
                break

            if Dictionary[Min + i] < Key:
                KQ = "False"
                break

            Dictionary[Min + i] -= Key

        if KQ == "False":
            break

with open("Hand of Straight.OUT", "w") as fout:
    fout.write(KQ)
    
    