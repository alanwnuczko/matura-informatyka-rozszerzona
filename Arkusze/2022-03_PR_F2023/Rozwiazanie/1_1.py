with open("szachy.txt") as f:
    plansze = f.read().strip().split("\n\n")

ile_plansz = 0
max_pustych = 0

for plansza in plansze:
    wiersze = plansza.splitlines()

    puste= 0

    for kolumna in range(8):
        pusta = True

        for wiersz in range(8):
            if wiersze[wiersz][kolumna] != '.':
                pusta = False
                break

        if pusta:
            puste += 1

    if puste > 0:
        ile_plansz += 1

    if puste > max_pustych:
        max_pustych = puste

print(ile_plansz, max_pustych)