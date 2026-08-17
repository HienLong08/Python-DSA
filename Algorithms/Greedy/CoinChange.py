# Coin Change - Greedy Algorithm
# Given a set of coin denominations and a target amount, always choose the largest possible coin.
# The goal is to use the minimum number of coins.
# Note: Greedy does not always guarantee the optimal solution.
# It works correctly for some coin systems but may fail for others.

with open("CoinChange.INP", "r") as fin:
    data = fin.readlines()
    N = int(data[0])
    Coins = list(map(int, data[1].split()))

Coins.sort(reverse=True)
Count = 0

for coin in Coins:
    Count += N // coin
    N %= coin

with open("CoinChange.OUT", "w") as fout:
    fout.write(str(Count))


# Example
N = 880
Coins = [500, 200, 100, 50, 20, 10]

Coins.sort(reverse=True)
Count = 0

for coin in Coins:
    Count += N // coin
    N %= coin

print(Count)

# Explanation:
# 880 // 500 = 1  -> remaining 380
# 380 // 200 = 1  -> remaining 180
# 180 // 100 = 1  -> remaining 80
# 80 // 50 = 1    -> remaining 30
# 30 // 20 = 1    -> remaining 10
# 10 // 10 = 1    -> remaining 0
# Total = 6 coins