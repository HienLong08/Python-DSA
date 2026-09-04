with open("Non-overlapping Intervals.INP", "r") as fin:
    data = fin.readlines()

n = int(data[0])
intervals = []

for i in range(1, n + 1):
    intervals.append(list(map(int, data[i].split())))

intervals.sort(key=lambda x: x[1])

Dem = 0
end = intervals[0][1]

for i in range(1, len(intervals)):
    start = intervals[i][0]

    if start < end:
        Dem += 1
    else:
        end = intervals[i][1]

with open("Non-overlapping Intervals.OUT", "w") as fout:
    fout.write(str(Dem))
    