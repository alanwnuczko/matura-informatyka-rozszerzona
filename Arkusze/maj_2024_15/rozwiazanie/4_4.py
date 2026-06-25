plansza = []

with open("plansza.txt") as f:
    for linia in f:
        plansza.append(list(map(int, linia.split())))

rozmiar_planszy = 100

liczba_jednomasztowcow_na_przekatnej = 0
liczba_dwumasztowcow_na_przekatnej = 0

for wiersz in range(rozmiar_planszy):
    for kolumna in range(rozmiar_planszy):

        if plansza[wiersz][kolumna] != 1:
            continue

        liczba_sasiadow = 0

        for przesuniecie_wiersza in (-1, 0, 1):
            for przesuniecie_kolumny in (-1, 0, 1):

                if przesuniecie_wiersza == 0 and przesuniecie_kolumny == 0:
                    continue

                sasiedni_wiersz = wiersz + przesuniecie_wiersza
                sasiednia_kolumna = kolumna + przesuniecie_kolumny

                if (0 <= sasiedni_wiersz < rozmiar_planszy and
                    0 <= sasiednia_kolumna < rozmiar_planszy and
                    plansza[sasiedni_wiersz][sasiednia_kolumna] == 1):

                    liczba_sasiadow += 1

        if liczba_sasiadow == 0:

            if (wiersz == kolumna or
                wiersz + kolumna == rozmiar_planszy - 1):

                liczba_jednomasztowcow_na_przekatnej += 1

        if (kolumna + 1 < rozmiar_planszy and
            plansza[wiersz][kolumna + 1] == 1):

            if (
                wiersz == kolumna or
                wiersz + kolumna == rozmiar_planszy - 1 or
                wiersz == kolumna + 1 or
                wiersz + (kolumna + 1) == rozmiar_planszy - 1
            ):
                liczba_dwumasztowcow_na_przekatnej += 1

        if (wiersz + 1 < rozmiar_planszy and
            plansza[wiersz + 1][kolumna] == 1):

            if (
                wiersz == kolumna or
                wiersz + kolumna == rozmiar_planszy - 1 or
                wiersz + 1 == kolumna or
                (wiersz + 1) + kolumna == rozmiar_planszy - 1
            ):
                liczba_dwumasztowcow_na_przekatnej += 1

print(liczba_jednomasztowcow_na_przekatnej)
print(liczba_dwumasztowcow_na_przekatnej)