import sys
try:
    t = int(input())
    for i in range(t):
        liczby = list(map(float, input().split()))
        liczby.pop(0)

        srednia = sum(liczby) / len(liczby)
        x = abs(srednia - liczby[0])

        closest = x
        liczba = liczby[0]

        for j in liczby:
            x = abs(srednia - j)
            if x < closest:
                closest = x
                liczba = j
                
        print(int(liczba))

except:
    sys.exit(77)