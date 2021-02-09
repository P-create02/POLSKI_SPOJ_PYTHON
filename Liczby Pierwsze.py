import sys
import math


def check(n):
    if n % 2 == 0 and n > 2 or n == 1:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


try:
    x = int(input())
    for i in range(0, x):
        num = int(input())
        if check(num):
            print('TAK')
        else:
            print('NIE')
except:
    sys.exit(0)
