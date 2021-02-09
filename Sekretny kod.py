import sys


try:

    t = int(input())

    for i in range(t):
        liczba = list(map(str, input().split()))
        counter = liczba[1].count('?') 
        wynik = 1

        if counter == 0:
            print('1')
        elif counter == 1 and len(liczba[1]) == 1:
            print('10')

        else:
            wynik *= 10 ** (counter)
            print(wynik)


except:
    sys.exit()