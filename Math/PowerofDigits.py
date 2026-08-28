with open("PowerofTwo.INP", "r") as fin:
    data = fin.readlines()
    n = int(data[0])

while n > 1 and n % 2 == 0:
    n //= 2

with open("PowerofTwo.OUT", "w") as fout:
    if n == 1:
        fout.write("true")
    else:
        fout.write("false")
    
    
