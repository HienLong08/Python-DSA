def MergeSort(Ds):
    if len(Ds) <= 1:
        return Ds

    Mid = len(Ds) // 2

    Left = MergeSort(Ds[:Mid])
    Right = MergeSort(Ds[Mid:])

    return Merge(Left, Right)

def Merge(Left, Right):
    Result = []
    i = 0
    j = 0

    while i < len(Left) and j < len(Right):
        if Left[i] < Right[j]:
            Result.append(Left[i])
            i += 1
        else:
            Result.append(Right[j])
            j += 1

    Result.extend(Left[i:])
    Result.extend(Right[j:])

    return Result

Ds = [8, 3, 5, 2, 7, 1]

print(MergeSort(Ds))