mniejsze = 0
wieksze = 0
rowne = 0
with open("liczby.txt") as f:
    for line in f:
        liczba_str = line.strip()
        liczba = int(liczba_str)

        cyfry = list(liczba_str)

        # print(f"Liczba: {cyfry}")
        # print(f"Najmniejsza: {int("".join(sorted(cyfry)))}")
        # print(f"Najwieksza: {int("".join(sorted(cyfry, reverse = True)))}")

        najmniejsza = int("".join(sorted(cyfry)))
        najwieksza = int("".join(sorted(cyfry, reverse = True)))

        wynik = najwieksza - najmniejsza
        if wynik == liczba:
            rowne += 1
            liczba_rowna = liczba
        elif wynik > liczba:
            wieksze += 1
        elif wynik < liczba:
            mniejsze += 1
    print(f"Równych: {rowne}, jest to {liczba_rowna}")
    print(f"Większych różnic: {wieksze}")
    print(f"Mniejszych różnic: {mniejsze}")
