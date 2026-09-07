with open("Coin Change.INP", "r") as fin:
    data = fin.readlines()
    coins = list(map(int, data[0].split()))
    amount = int(data[1])
    
Dp = [999999] * (amount + 1)
Dp[0] = 0

for i in range(amount + 1):
    for coin in coins:
        if coin <= i:
            Dp[i] =min(Dp[i], Dp[i - coin] + 1)
            
with open("Coin Change.OUT", "w") as fout:
    if Dp[amount] == 999999:
        fout.writelines("-1")
    else:
        fout.writelines(str(Dp[amount]))
