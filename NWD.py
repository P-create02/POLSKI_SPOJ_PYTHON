t = int(input())
for i in range(t):
    x = input()
    tab = []
    tekst = x.split(' ')
    a = int(tekst[0])
    b = int(tekst[1])
    if 0 <= a and b <= 1000000:
        while b:
            a, b = b, a % b
        print(a)
