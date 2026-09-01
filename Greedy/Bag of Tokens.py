with open("Bags of Token.INP", "r") as fin:
    data = fin.readlines()
    tokens = list(map(int, data[0].split()))
    power = int(data[1])

tokens.sort()

left = 0
right = len(tokens) - 1
score = 0
Max = 0

while left <= right:
    if power >= tokens[left]:
        power -= tokens[left]
        score += 1
        left += 1
        Max = max(Max, score)

    elif score > 0:
        power += tokens[right]
        score -= 1
        right -= 1

    else:
        break

with open("Bags of Token.OUT", "w") as fout:
    fout.write(str(Max))