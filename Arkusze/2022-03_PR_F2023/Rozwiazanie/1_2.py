with open("szachy.txt") as f:
    plansze = f.read().strip().split("\n\n")

ile = 0
min_bierek = 64

for plansza in plansze:
    wiersze = plansza.splitlines()

    biale = {
        'K': 0,
        'H': 0,
        'W': 0,
        'G': 0,
        'S': 0,
        'P': 0
    }

    czarne = {
        'k': 0,
        'h': 0,
        'w': 0,
        'g': 0,
        's': 0,
        'p': 0
    }

    for wiersz in wiersze:
        for znak in wiersz:
            if znak in biale:
                biale[znak] += 1
            elif znak in czarne:
                czarne[znak] += 1

    rownowaga = True

    for figura in "KHWGSP":
        if biale[figura] != czarne[figura.lower()]:
            rownowaga = False
            break

    if rownowaga:
        ile += 1
        liczba_bierek = sum(biale.values()) + sum(czarne.values())

        if liczba_bierek < min_bierek:
            min_bierek = liczba_bierek

print(ile, min_bierek)