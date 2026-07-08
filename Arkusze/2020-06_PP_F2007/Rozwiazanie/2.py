# 2_1:
bilet_tercja = int("2210", 3)
bilet_kwinta = int("321", 5)

bilet_tercja_osemkowo = oct(bilet_tercja)[2:]
bilet_kwinta_osemkowo = oct(bilet_kwinta)[2:]
print(bilet_tercja_osemkowo)
print(bilet_kwinta_osemkowo)

# 2_2:
def na_trojkowy(n):
    if n == 0:
        return "0"
    wynik = ""
    while n > 0:
        wynik = str(n % 3) + wynik
        n //= 3
    return wynik

def na_piatkowy(n):
    if n == 0:
        return "0"
    wynik = ""
    while n > 0:
        wynik = str(n % 5) + wynik
        n //= 5
    return wynik

roznica_cen = bilet_kwinta - bilet_tercja

roznica_kwintolandia = na_piatkowy(roznica_cen)
roznica_tercjolandia = na_trojkowy(roznica_cen)

print(roznica_kwintolandia)
print(roznica_tercjolandia)