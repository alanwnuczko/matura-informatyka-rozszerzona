wnetrze = 0
with open("punkty.txt") as f:
    for line in f:
        x, y = map(int, line.split())

        odleglosc = (x - 200) ** 2 + (y - 200) ** 2

        if odleglosc < 200 ** 2:
            wnetrze += 1
        elif odleglosc == 200 ** 2:
            print(x, y)

print("Liczba punktów wewnątrz koła:", wnetrze)