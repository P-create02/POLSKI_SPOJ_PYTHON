t = int(input())
for i in range(t):
    wprowadzane = input()
    pierwsza_liczba = int(wprowadzane[0])

    for j in range(len(wprowadzane)):
        if wprowadzane[j] == "+":
            pierwsza_liczba += int(wprowadzane[j+1])
        elif wprowadzane[j] == "-":
            pierwsza_liczba -= int(wprowadzane[j+1])

    print(pierwsza_liczba)