with open("Best Time to Buy and Sell Stock II.INP", "r") as fin:
    data = fin.readlines()
    prices = list(map(int, data[0].split()))
    
profit = 0

for i in range(1, len(prices)):
    if prices[i] > prices[i - 1]:
        profit += prices[i] - prices[i - 1]
        
with open("Best Time to Buy and Sell Stock II.OUT", "w") as fout:
    fout.writelines(str(profit))