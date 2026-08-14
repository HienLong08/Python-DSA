def SelectionSort(Ds):
    N = len(Ds)

    for i in range(N):
        MinIndex = i

        for j in range(i + 1, N):
            if Ds[j] < Ds[MinIndex]:
                MinIndex = j

        Ds[i], Ds[MinIndex] = Ds[MinIndex], Ds[i]

    return Ds


Ds = [5, 3, 8, 1, 2]
print(SelectionSort(Ds))