with open("FibonacciNumber.INP", "r") as fin:
    data = fin.readlines()
    n = int(data[0])

with open("FibonacciNumber.OUT", "w") as fout:
    if n == 0:
        fout.writelines("0")
    
    if n == 1:
        fout.writelines("1")
    
    if n > 1:
        Ds = [0] * (n + 1)
        Ds[1] = 1

        for i in range(2, n + 1):
            Ds[i] = Ds[i - 1] + Ds[i - 2]

        fout.writelines(str(Ds[n]))