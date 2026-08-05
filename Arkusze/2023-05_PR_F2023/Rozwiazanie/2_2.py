wynik = 0
def licz_bloki(n):
    liczba_blokow = 1
    liczba_binarna = list(n)
    for i in range(1, len(liczba_binarna)):
        if liczba_binarna[i] != liczba_binarna[i-1]:
            liczba_blokow += 1
    return liczba_blokow

with open("bin.txt") as f:
    for line in f:
        n = line.strip()
        if licz_bloki(n) <= 2:
            wynik += 1

print(wynik)