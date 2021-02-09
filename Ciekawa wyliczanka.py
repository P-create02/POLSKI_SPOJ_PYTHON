import math

S = 0
n = 0
w = 1

liczba = int(input())

while S < liczba:
    S += math.pow(2, w)
    n += 1
    w += 1

temp = (math.pow(2, n) - (S-liczba))


liczby_tworzace_liczbe = [] 
i = n
while i > 0:
    wynik = math.ceil(temp / math.pow(2, i-1)) 
    if wynik % 2 == 0:
        liczby_tworzace_liczbe.append(6)
        i -= 1
    else:
        liczby_tworzace_liczbe.append(5)
        i -= 1

result = ''.join(map(str, liczby_tworzace_liczbe)) 
print(result)