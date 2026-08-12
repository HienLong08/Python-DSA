def BinarySearch(Ds, Target):
    Left = 0
    Right = len(Ds) - 1

    while Left <= Right:
        Mid = (Left + Right) // 2

        if Ds[Mid] == Target:
            return Mid

        if Ds[Mid] < Target:
            Left = Mid + 1
        else:
            Right = Mid - 1

    return -1
