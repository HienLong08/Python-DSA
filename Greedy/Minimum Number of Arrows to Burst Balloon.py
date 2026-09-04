with open("Minimum Number of Arrows to Burst Balloon.INP", "r") as fin:
    data = fin.readlines()
    n = int(data[0])
    points = []

for i in range(1, n + 1):
    balloon = list(map(int, data[i].split()))
    points.append(balloon)

points.sort(key=lambda x: x[1])

Dem = 1
end = points[0][1]

for i in range(1, len(points)):
    start = points[i][0]

    if start > end:
        Dem += 1
        end = points[i][1]

with open("Minimum Number of Arrows to Burst Balloon.OUT", "w") as fout:
    fout.write(str(Dem))