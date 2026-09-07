with open("Dota2 Senate.INP", "r") as fin:
    data = fin.readlines()
    senate = str(data[0].strip())

from collections import deque

Radiant = deque()
Dire = deque()

for i in range(len(senate)):
    if senate[i] == "R":
        Radiant.append(i)
    if senate[i] == "D":
        Dire.append(i)

while len(Radiant) > 0 and len(Dire) > 0:
    if Radiant[0] < Dire[0]:
        r = Radiant.popleft()
        Dire.popleft()
        Radiant.append(r + len(senate))

    else:
        d = Dire.popleft()
        Radiant.popleft()
        Dire.append(d + len(senate))

with open("Dota2 Senate.OUT", "w") as fout:
    if len(Radiant) > 0:
        fout.write("Radiant")
    else:
        fout.write("Dire")
        Dire.append(d + len(senate))
        
    
