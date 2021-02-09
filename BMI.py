def BMI(x, y):
    y /= 100
    return x / y**2



niedowaga = []
wart_praw = []
nadwaga = []
t = int(input())

for i in range(t):
    imie, kg, cm = map(str, input().split())
    bmi = BMI(int(kg), int(cm))

    if bmi < 18.5:
        niedowaga.append(imie)
    elif bmi >= 18.5 and bmi < 25:
        wart_praw.append(imie)
    else:
        nadwaga.append(imie)


print("niedowaga")
print('\n'.join(niedowaga))
print()
print("wartosc prawidlowa")
print('\n'.join(wart_praw))
print()
print("nadwaga")
print('\n'.join(nadwaga))
print()