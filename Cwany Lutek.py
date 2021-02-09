def silnia_rek(n):
    if n > 1:
        return n * silnia_rek(n-1)
    elif n in (0,1):
        return 1
    else:
        return 0



t = int(input())
for i in range(t):
    n, k = input().split()
    w = int(n) - int(k)

    x = silnia_rek(int(n))
    y = silnia_rek(int(k))
    z = silnia_rek(int(w))

    try:
        symbol_newtona = x / (y * z)

        if symbol_newtona % 2 == 0:
            print("P")
        else:
            print("N")

    except ZeroDivisionError:
        print("N")