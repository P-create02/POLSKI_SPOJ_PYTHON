t = int(input())

for i in range(t):
    liczba = input()
    ile = 0
    
    if liczba == liczba[::-1]:
        print('%s %s' %(liczba, ile))
    else:
        while liczba != liczba[::-1]:
            ile += 1
            liczba, odwrotna = int(liczba), int(liczba[::-1])
            liczba += odwrotna
            liczba = str(liczba)
        print('%s %s' %(liczba,ile))