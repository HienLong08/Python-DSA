# Given an m x n grid, a robot starts at the top-left corner
# and wants to reach the bottom-right corner.
# The robot can only move right or down.
# Find the number of unique paths the robot can take to reach the destination.

with open("UniquePath.INP", "r") as fin:
    data = fin.readlines()
    m, n = map(int, data[0].split())

Ds = [[1] * n for _ in range(m)]

for i in range(1, m):
    for j in range(1, n):
        Ds[i][j] = Ds[i-1][j] + Ds[i][j-1]

Result = Ds[m - 1][n - 1]

with open("UniquePath.OUT", "w") as fout:
    fout.write(str(Result))

print(Result)