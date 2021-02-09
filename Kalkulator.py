import sys

try:
    while True:
        result = list(map(str, input().split()))
        if result != '':
            if (result[0] == '+'):
                print(int(result[1])+int(result[2]))
            elif (result[0] == '-'):
                print(int(result[1])-int(result[2]))
            elif (result[0] == '*'):
                print(int(result[1])*int(result[2]))
            elif (result[0] == '/'):
                print(int(int(result[1])/int(result[2])))
            elif (result[0] == '%'):
                print(int(result[1]) % int(result[2]))
            else:
                break
except:
    sys.exit(0)
