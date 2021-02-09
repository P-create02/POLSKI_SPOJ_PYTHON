def Factorial(k):
    wyn = 1
    for j in range(1, k + 1):
        wyn *= j
    return wyn


def Newton(n, k):
    wynik = 1
    if n == k:
        return 1
    if k == 0:
        return 1
    for i in range(k):
        wynik *= n - i
    return int(wynik / Factorial(k))


t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(Newton(a, b))