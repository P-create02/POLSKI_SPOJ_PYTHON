t = int(input())
liczby = []
for i in range(t):
    liczba = input()
    liczby.append(liczba)

str(input()) 

t2 = int(input())
for j in range(t2):
    liczby_warunkowe = int(input())
    ilosc_liczb = len(liczby)
    ile_liczb_pasuje = []

    if liczby_warunkowe == 0:
        print(0)

    else:
        for n in range(ilosc_liczb):
            if int(liczby[n]) < liczby_warunkowe:
                ile_liczb_pasuje.append(liczby[n])
        print(len(ile_liczb_pasuje))