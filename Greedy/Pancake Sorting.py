with open("Pancake Sorting.INP", "r") as fin:
    data = fin.readlines()
    arr = list(map(int, data[0].split()))

Ds = []
K = len(arr)

while K > 1:
    Max = max(arr[:K])
    Pos = arr.index(Max)

    if Pos != 0:
        arr[:Pos + 1] = arr[:Pos + 1][::-1]
        Ds.append(Pos + 1)

    if K != 1:
        arr[:K] = arr[:K][::-1]
        Ds.append(K)

    K -= 1

with open("Pancake Sorting.OUT", "w") as fout:
    fout.write(" ".join(str(x) for x in Ds))
        
        
    
    