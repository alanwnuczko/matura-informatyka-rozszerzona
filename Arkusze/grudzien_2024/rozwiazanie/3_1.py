licznik = 0
liczby_wynik = []
with open("liczby.txt") as f:
    for line in f:
        x = int(line)
        i = 1

        while i * i < x:
            i += 1

        if i * i == x:
            licznik += 1
            liczby_wynik.append(line)


print(licznik, liczby_wynik[0])