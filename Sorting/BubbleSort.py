def BubbleSort(Ds):
    N = len(Ds)
    for i in range(N):
        for j in range(0, N - i -1):
            if Ds[j] > Ds[j+1]:
                Ds[j], Ds[j+1] = Ds[j+1], Ds[j]
    return Ds

Ds = [5, 3, 8, 4, 2]

print(BubbleSort(Ds))
