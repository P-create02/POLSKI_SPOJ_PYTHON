ile = int(input())

for i in range(ile):
    liczby = list(map(int, input().split()))
    segmenty = liczby[0] - 1
    liczby.pop(0)
    nogi = sum(liczby)
    print(segmenty + nogi)