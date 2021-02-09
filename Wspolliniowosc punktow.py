import sys

def czy_punkty_w_jednej_lini(x1,y1,x2,y2,x3,y3):
    if x2 - x1 == 0:
        AB = 0
    else:
        AB = (y2 - y1) / (x2 - x1)
    if x3 - x2 == 0:
        BC = 0
    else:
        BC = (y3 - y2) / (x3 - x2)
    if AB == BC:
        print('TAK')
    else:
        print('NIE')


try:
    t = int(input())

    for i in range(t):
        punkty = list(map(int, input().split()))
        czy_punkty_w_jednej_lini(punkty[0], punkty[1],punkty[2],punkty[3],punkty[4],punkty[5],)
except:
    sys.exit(22)