x = input()
x = x.split(" ")
a = int(x[0])
b = int(x[1])

liczby = input()
liczby = liczby.split(" ")
liczby1 = liczby[b:]
liczby2 = liczby[:b]
print(" ".join(liczby1+liczby2))