# Best Time to Buy and Sell Stock
# Cho mảng prices, trong đó prices[i] là giá cổ phiếu vào ngày i.
# Ta cần chọn một ngày để mua và một ngày khác trong tương lai để bán.
# Mục tiêu là tối đa hóa lợi nhuận = giá bán - giá mua.
# Ngày mua phải đứng trước ngày bán.
# Nếu không thể tạo ra lợi nhuận, trả về 0.
#
# Ví dụ:
# prices = [7, 1, 5, 3, 6, 4]
# Mua với giá 1 và bán với giá 6 -> lợi nhuận = 6 - 1 = 5

with open("BestTimetoBuyandSellStock.INP", "r") as fin:
    data = fin.readlines()
    prices = list(map(int, data[0].split()))
    
Min = prices[0]
cash = 0
    
for price in prices:
    Min = min(Min, price)
    cash = max(cash, price - Min)
    
with open("BestTimetoBuyandSellStock.OUT", "w") as fout:
    fout.writelines(str(cash))
    
print(cash)

    
