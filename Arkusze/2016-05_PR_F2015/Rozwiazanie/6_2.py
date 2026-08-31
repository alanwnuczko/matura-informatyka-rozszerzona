def odszyfruj(slowo, k):
    wynik = ""

    for znak in slowo:
        wynik += chr((ord(znak) - 65 - k) % 26 + 65)

    return wynik

with open("dane_6_2.txt") as f, open("wyniki_6_2.txt", "w") as g:
    for line in f:
        slowo, k = line.split()
        g.write(odszyfruj(slowo, int(k)) + "\n")