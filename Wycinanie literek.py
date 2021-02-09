import sys

try:
    while True:

        literki = list(map(str, input().split()))
        if literki != '':
            tekst = ''
            for i in literki[1]:
                if i != literki[0]:
                    tekst += i
                    
            print(tekst)

        else:
            break

except:
    sys.exit()