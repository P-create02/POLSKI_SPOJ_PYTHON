import sys

try:
    A = False
    for linia in sys.stdin:
        tekst = list(map(str, linia))

        for i in range(0, len(tekst)):
            if tekst[i] == "<":
                A = True
            elif tekst[i] == ">":
                A = False
            if (A):
                tekst[i] = tekst[i].upper()

        tekst = "".join(tekst)
        print(tekst)

except:
    sys.exit()