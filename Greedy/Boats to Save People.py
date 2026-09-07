with open("Boats to Save People.INP", "r") as fin:
    data = fin.readlines()
    people = list(map(int, data[0].split()))
    limit = int(data[1])
    
Dem = 0
Right = len(people) - 1
Left = 0

people.sort

while Right >= Left:
    if people[Right] + people[Left] <= limit:
        Dem += 1
        Right -= 1
        Left += 1
    else:
        Right -= 1
        Dem += 1
        
with open("Boat to Save People.OUT", "w") as fout:
    fout.writelines(str(Dem))