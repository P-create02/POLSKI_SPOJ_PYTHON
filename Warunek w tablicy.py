import sys
try:
    
    while True:
        dane = list(map(str, input().split()))
        if dane != '':
            liczby = [].append(dane[:len(dane)-2])
            znak = [].append(dane[-2:-1])
            liczba = [].append(dane[-1:])
    
            if znak == ">":
                print(dane > liczba)
            elif znak == "<":
                print(dane < liczba)
    
        else:
            break
except:
    sys.exit()