ile = int(input())
i = 0
for i in range(ile):
    liczby = input()
    liczba = liczby.split(" ")
    parzyste = liczba[1::2]
    nieparzysta = liczba[2::2]
    print(" ".join(parzyste+nieparzysta))
