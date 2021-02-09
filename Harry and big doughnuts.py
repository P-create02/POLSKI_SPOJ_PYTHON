ile_t = int(input())

for i in range(ile_t):
    dane = input().split()
    c = int(dane[0])
    k = int(dane[1])
    w = int(dane[2])

    if c * w <= k:
        print("yes")
    else:
        print("no")