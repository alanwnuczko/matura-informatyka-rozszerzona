# Dla wyrazów wczytanych z pliku:
with open("wyrazy.txt") as f:
    for wyraz in f:
        wyraz = wyraz.strip()
        if wyraz == wyraz[::-1]:
            print(wyraz)

# Sprawdzanie czy słowo jest palindromem
def czy_palindrom(slowo):
    return slowo == slowo[::-1]

print(czy_palindrom("kajak")) # Zwraca True
print(czy_palindrom("python")) # Zwraca False