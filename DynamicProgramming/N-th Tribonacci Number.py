with open("N-th Tribonacci Number.INP", "r") as fin:
    data = fin.readlines()
    n = int(data[0])

Dp = [0] * (n + 1)

with open("N-th Tribonacci Number.OUT", "w") as fout:
    if n == 0:
        fout.writelines("0")
    elif n == 1:
        fout.writelines("1")
    elif n == 2:
        fout.writelines("1")
    else:
        Dp[0] = 0
        Dp[1] = 1
        Dp[2] = 1

        for i in range(3, n + 1):
            Dp[i] = Dp[i - 1] + Dp[i - 2] + Dp[i - 3]

        fout.writelines(str(Dp[n]))