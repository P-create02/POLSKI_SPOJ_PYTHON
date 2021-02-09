while True:
    tekst = input()
    if tekst != ' ':
        print(tekst.title().replace(' ', ''))
    else:
        break