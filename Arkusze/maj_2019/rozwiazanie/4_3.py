from math import gcd

with open("liczby.txt") as f:
    liczby = [int(x) for x in f]

naj_dl = 0
pierwsza = 0
naj_nwd = 0

for i in range(len(liczby)):
    aktualny_nwd = liczby[i]

    for j in range(i, len(liczby)):
        aktualny_nwd = gcd(aktualny_nwd, liczby[j])

        if aktualny_nwd == 1:
            break

        dlugosc = j - i + 1

        if dlugosc > naj_dl:
            naj_dl = dlugosc
            pierwsza = liczby[i]
            naj_nwd = aktualny_nwd

print("Pierwsza liczba:", pierwsza)
print("Długość:", naj_dl)
print("NWD:", naj_nwd)