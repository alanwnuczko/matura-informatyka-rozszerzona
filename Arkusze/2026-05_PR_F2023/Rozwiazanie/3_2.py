def W(s1, s2):
    suma = 0

    for litera in "abcdefghijklmnopqrstuvwxyz":
        suma += min(s1.count(litera), s2.count(litera))

    return suma

maks = 0
wynik = []

with open("pary.txt") as file:
    for line in file:
        s1, s2 = line.split()

        w = W(s1, s2)

        if w > maks:
            maks = w
            wynik = [s1, s2]

print(wynik[0], wynik[1], maks)