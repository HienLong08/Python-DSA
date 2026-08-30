with open("AssignCookies.INP", "r") as fin:
    data = fin.readlines()
    g = list(map(int, data[0].split()))
    s = list(map(int, data[1].split()))
    
g.sort()
s.sort()

Count = 0
Pointer = 0

for i in s:
    if Pointer < len(g) and i >= g[Pointer]:
        Count += 1
        Pointer += 1

with open("AssignCookies.OUT", "w") as fout:
    fout.writelines(str(Count))