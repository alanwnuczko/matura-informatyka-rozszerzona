with open("liczby.txt") as f:
    liczby = list(map(int, f.readline().split()))

najwyzsza_srednia = 0
najlepsza_dlugosc = 0
pierwszy_element = 0

for poczatek in range(len(liczby)):
    suma = 0

    for koniec in range(poczatek, len(liczby)):
        suma += liczby[koniec]
        dlugosc = koniec - poczatek + 1

        if dlugosc >= 50:
            srednia = suma / dlugosc

            if srednia > najwyzsza_srednia:
                najwyzsza_srednia = srednia
                najlepsza_dlugosc = dlugosc
                pierwszy_element = liczby[poczatek]

print(najwyzsza_srednia)
print(najlepsza_dlugosc)
print(pierwszy_element)