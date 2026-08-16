def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

with open("dane.txt") as f:
    napis = f.read().strip()

n = len(napis)
wynik = ""

for dlugosc in range(n, 1, -2):
    for i in range(0, n - dlugosc + 1, 2):
        fragment = napis[i:i + dlugosc]

        if czy_pierwsza(sum(ord(c) for c in fragment)):
            wynik = fragment
            break

    if wynik:
        break

print(wynik)