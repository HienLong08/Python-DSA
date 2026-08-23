# Trapping Rain Water
# Given n non-negative integers representing the height of columns,
# where each column has a width of 1, calculate how much rainwater can be trapped.
# Example:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation:
# Water can be trapped between taller columns.
# For each position, the trapped water depends on the tallest column
# on its left and the tallest column on its right.
# The total amount of trapped rainwater is 6 units.

with open("TrappingRainWater.INP", "r") as fin:
    data = fin.readlines()
    height = list(map(int, data[0].split()))

N = len(height)

LeftMax = [0] * N
RightMax = [0] * N

LeftMax[0] = height[0]

for i in range(1, N):
    LeftMax[i] = max(LeftMax[i - 1], height[i])

RightMax[N - 1] = height[N - 1]

for i in range(N - 2, -1, -1):
    RightMax[i] = max(RightMax[i + 1], height[i])

Sum = 0

for i in range(N):
    Water = min(LeftMax[i], RightMax[i]) - height[i]
    Sum += Water

with open("TrappingRainWater.OUT", "w") as fout:
    fout.write(str(Sum))

print(Sum)