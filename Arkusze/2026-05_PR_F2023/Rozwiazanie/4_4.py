with open("korpo.txt") as f:
    szef = [0]

    for line in f:
        szef.append(int(line))

maks_przelozonych = 0
ile_pracownikow = 0

for i in range(1, len(szef)):
    licznik = 0
    pracownik = i

    while szef[pracownik] != 0:
        licznik += 1
        pracownik = szef[pracownik]

    if licznik > maks_przelozonych:
        maks_przelozonych = licznik
        ile_pracownikow = 1

    elif licznik == maks_przelozonych:
        ile_pracownikow += 1

print(maks_przelozonych, ile_pracownikow)