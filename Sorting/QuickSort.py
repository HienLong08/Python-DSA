def QuickSort(Ds):
    if len(Ds) <= 1:
        return Ds

    Pivot = Ds[len(Ds) // 2]
    Left = []
    Middle = []
    Right = []

    for x in Ds:
        if x < Pivot:
            Left.append(x)
        elif x == Pivot:
            Middle.append(x)
        else:
            Right.append(x)

    return QuickSort(Left) + Middle + QuickSort(Right)


Ds = [8, 3, 5, 4, 7, 6, 1, 2]

print(QuickSort(Ds))