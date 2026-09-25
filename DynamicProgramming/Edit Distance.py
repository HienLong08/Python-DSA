with open("Edit Distance.INP", "r") as fin:
    data = fin.readlines()
    word1 = str(data[0])
    word2 = str(data[1])
    
m = len(word1)
n = len(word2)

m, n = len(word1), len(word2)
Dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(m + 1):
    dp[i][0] = i
for j in range(n + 1):
    dp[0][j] = j
    
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if word1[i - 1] = word2[j - 1]:
            Dp[i][j] = Dp[i - 1][j - 1]:
        else:
            
            
