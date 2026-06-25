plansza = []

with open("plansza.txt") as f:
    for linia in f:
        plansza.append(list(map(int, linia.split())))

rozmiar_planszy = 100

jednomasztowce = [[False] * rozmiar_planszy for _ in range(rozmiar_planszy)]

for wiersz in range(rozmiar_planszy):
    for kolumna in range(rozmiar_planszy):

        if plansza[wiersz][kolumna] == 1:

            czy_jednomasztowiec = True

            for przesuniecie_wiersza in (-1, 0, 1):
                for przesuniecie_kolumny in (-1, 0, 1):

                    if przesuniecie_wiersza == 0 and przesuniecie_kolumny == 0:
                        continue

                    sasiedni_wiersz = wiersz + przesuniecie_wiersza
                    sasiednia_kolumna = kolumna + przesuniecie_kolumny

                    if (0 <= sasiedni_wiersz < rozmiar_planszy and
                        0 <= sasiednia_kolumna < rozmiar_planszy and
                        plansza[sasiedni_wiersz][sasiednia_kolumna] == 1):

                        czy_jednomasztowiec = False

            if czy_jednomasztowiec:
                jednomasztowce[wiersz][kolumna] = True

liczba_par_symetrycznych = 0

for wiersz in range(rozmiar_planszy):
    for kolumna in range(wiersz + 1, rozmiar_planszy):

        if (jednomasztowce[wiersz][kolumna] and
            jednomasztowce[kolumna][wiersz]):

            liczba_par_symetrycznych += 1

print(liczba_par_symetrycznych)