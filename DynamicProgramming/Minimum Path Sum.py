with open("Minimum Path Sum.INP", "r") as fin:
    data = fin.readlines()
    m, n = map(int, data[0].split())

Grids = []

for i in range(1, m + 1):
    Grid = list(map(int, data[i].split()))
    Grids.append(Grid)
    
Dp = [[0] * n for _ in range(m)]

Dp[0][0] = Grids[0][0]

for j in range(1, n):
    Dp[0][j] = Dp[0][j - 1] + Grids[0][j]

for i in range(1, m):
    Dp[i][0] = Dp[i - 1][0] + Grids[i][0]

for i in range(1, m):
    for j in range(1, n):
        Dp[i][j] = min(Dp[i - 1][j] + Dp[i][j - 1]) + Grids[i][j]
        
with open("Minimum Path Sum.OUT", "w") as fout:
    fout.write(str(Dp[m - 1][n - 1]))