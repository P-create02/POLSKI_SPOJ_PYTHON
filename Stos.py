import sys
try:
    stos = []
    while True:
        znak = str(input())
        if znak != '':
            if znak == "+":
                if len(stos) < 10:
                    stos.insert(0, int(input()))
                    print(":)")
                else:
                    print(":(")
            elif znak == "-":
                if not stos:
                    print(":(")
                else:
                    print(stos[0])
                    stos.pop(0)

        else:
            break
except:
    sys.exit(0)