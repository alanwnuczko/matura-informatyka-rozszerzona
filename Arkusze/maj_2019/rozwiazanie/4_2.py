def silnia(n):
    wynik = 1
    for i in range(2, n+1):
        wynik *= i
    return wynik
f = open("liczby.txt")

for wiersz in f:
    liczba = int(wiersz)

    suma = 0
    for cyfra in str(liczba):
        suma += silnia(int(cyfra))

    if suma == liczba:
        print(liczba)
f.close()