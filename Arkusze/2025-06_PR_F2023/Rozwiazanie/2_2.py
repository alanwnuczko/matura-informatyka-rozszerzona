import math

def liczba_cyfr(n):
    cyfry = 0
    while n > 0:
        cyfry += 1
        n //= 10
    return cyfry

def dwie_liczby(k):
    cyfry = liczba_cyfr(k)
    p = 1
    i = 0
    while i < cyfry // 2:
        p *= 10
        i += 1

    a = k // p
    b = k % p

    return a, b

licznik = 0
with open("liczby1.txt") as f:
    for line in f:
        liczba = int(line.strip())

        a, b = dwie_liczby(liczba)

        if math.gcd(a, b) == 1:
            licznik += 1

print(licznik)