def Najwiekszy_Czynnik(n):
    d = 2
    wynik = 1

    while n > 1:
        while n % d == 0:
            wynik = d
            n = n // d
        d = d + 1

    return wynik

print(Najwiekszy_Czynnik(252))