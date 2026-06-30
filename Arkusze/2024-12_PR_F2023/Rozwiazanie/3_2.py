def czy_pierwsza(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

with open("liczby.txt") as f:
    for line in f:
        line = int(line)
        licznik = 0
        for dzielnik in range(1, line + 1):
            if line % dzielnik == 0 and czy_pierwsza(dzielnik):
                licznik += 1

        if licznik >= 5:
                    print(line)

