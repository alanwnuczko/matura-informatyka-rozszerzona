import math

liczby = []
wzglednie_pierwsze = []
with open("liczby.txt") as f:
    for line in f:
        liczby.append(int(line.strip()))

for liczba in liczby:
    czy_wzglednie_pierwsza = True

    for inna in liczby:
        if liczba != inna:
            if math.gcd(liczba, inna) != 1:
                czy_wzglednie_pierwsza = False

    if czy_wzglednie_pierwsza:
        wzglednie_pierwsze.append(liczba)

print(max(wzglednie_pierwsze))