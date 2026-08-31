licznik = 0

with open("liczby.txt") as f:
    for line in f:
        liczba = list(line.strip())

        licznik_0 = 0
        licznik_1 = 0
        for i in liczba:

            if i == "0":
                licznik_0 += 1
            else:
                licznik_1 += 1

        if licznik_0 > licznik_1:
            licznik += 1

print(licznik) # Wynik: 422