licznik_mod_2 = 0
licznik_mod_8 = 0

with open("liczby.txt") as f:
    for line in f:
        liczba = int(line.strip(), 2)

        if liczba % 2 == 0:
            licznik_mod_2 += 1

        if liczba % 8 == 0:
            licznik_mod_8 += 1

print(licznik_mod_2) # Wynik: 500
print(licznik_mod_8) # Wynik: 123