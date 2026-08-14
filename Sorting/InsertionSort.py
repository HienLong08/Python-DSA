def InsertionSort(Ds):
    N = len(Ds)

    for i in range(1, N):
        Key = Ds[i]
        j = i - 1

        while j >= 0 and Ds[j] > Key:
            Ds[j + 1] = Ds[j]
            j -= 1

        Ds[j + 1] = Key

    return Ds


Ds = [5, 3, 8, 1, 2]

print(InsertionSort(Ds))