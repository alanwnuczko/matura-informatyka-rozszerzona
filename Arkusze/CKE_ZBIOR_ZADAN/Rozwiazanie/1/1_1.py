def wynik(i):
    if i < 3:
        return 1
    else:
        if i % 2 == 0:
            return wynik(i - 3) + wynik(i - 1) + 1
        else:
            return wynik(i - 1) % 7

# 1_1:
print(wynik(2))
print(wynik(3))
print(wynik(4))
print(wynik(5))
print(wynik(6))
print(wynik(7))
print(wynik(8))