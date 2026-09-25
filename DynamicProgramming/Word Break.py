with open("Word Break.INP", "r") as fin:
    data = fin.readlines()

    s = data[0].strip()
    N = int(data[1])

    Ds = []

    for i in range(N):
        Ds.append(data[i + 2].strip())


DP = [False] * (len(s) + 1)
DP[0] = True

for i in range(1, len(s) + 1):
    for j in range(i):
        Word = s[j:i]

        if DP[j] and Word in Ds:
            DP[i] = True
            break


with open("Word Break.OUT", "w") as fout:
    if DP[len(s)]:
        fout.writelines("YES")
    else:
        fout.writelines("NO")