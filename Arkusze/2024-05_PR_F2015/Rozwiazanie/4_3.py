plansza = []

with open("plansza.txt") as f:
    for linia in f:
        plansza.append(list(map(int, linia.split())))

rozmiar_planszy = 100

liczba_dwumasztowcow = 0

for wiersz in range(rozmiar_planszy):
    for kolumna in range(rozmiar_planszy):

        if plansza[wiersz][kolumna] == 1:

            if (kolumna + 1 < rozmiar_planszy and
                plansza[wiersz][kolumna + 1] == 1):
                liczba_dwumasztowcow += 1

            if (wiersz + 1 < rozmiar_planszy and
                plansza[wiersz + 1][kolumna] == 1):
                liczba_dwumasztowcow += 1

print(liczba_dwumasztowcow)