import sys
try:
    pierwszy = True
    wczesniejszy = 0
    liczba = 0
    while True:
        liczby = int(input())
        print(liczby)
        if liczby == 42 and wczesniejszy != 42 and not pierwszy:
            liczba += 1
        if liczba == 3:
            break
        wczesniejszy = liczby
        pierwszy = False
except:
    sys.exit()