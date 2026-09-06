from math import gcd

licznik = 0

with open("liczby.txt") as f:
    for line in f:
        M, a, b = map(int, line.split())

        if gcd(M, a) == 1:
            licznik += 1

print(licznik)