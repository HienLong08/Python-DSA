with open("Max Chunks to Make Sorted.INP", "r") as fin:
    data = fin.readlines()
    arr = list(map(int, data[0].split()))
    
Dem = 0
Max = 0

for i in range(len(arr)):
    Max = max(Max, arr[i])
    if Max == i:
        Dem += 1
        Max = 0
        
with open("Max Chunks to Make Sorted.OUT", "w") as fout:
    fout.writelines(str(Dem))
    