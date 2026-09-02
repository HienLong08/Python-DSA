with open("Partition Labels.INP", "r") as fin:
    data = fin.readlines()
    s = data[0].strip()

Dictionary = {}
Ds = []
MaxReal = 0
start = 0

for i in range(len(s)):
    Dictionary[s[i]] = i

for i in range(len(s)):
    MaxReal = max(MaxReal, Dictionary[s[i]])

    if MaxReal == i:
        Ds.append(i - start + 1)
        start = i + 1

with open("Partition Labels.OUT", "w") as fout:
    fout.write(" ".join(str(x) for x in Ds))
    
    
    

