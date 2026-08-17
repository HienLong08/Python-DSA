def Heaptify(Ds, N, i):
    Max = i
    Left = 2*i + 1
    Right = 2*i + 2
    if Left < N and Ds[Left] > Ds[Max]:
        Max = Left
    if Right < N and Ds[Right] > Ds[Max]:
        Max = Right
        
    if Max != i:
        Ds[i], Ds[Max] = Ds[Max], Ds[i]
        Heaptify(Ds, N, Max)
        
def HeapSort(Ds):
    N = len(Ds)
    for i in range(N//2 - 1, -1, -1):
        Heaptify(Ds, N, i)
    for i in range(N - 1, 0, -1):
        Ds[0], Ds[i] = Ds[i], Ds[0]
        Heaptify(Ds, i, 0)
    
    return Ds

Ds = [8, 3, 5, 4, 7, 6, 1, 2]

print(HeapSort(Ds))