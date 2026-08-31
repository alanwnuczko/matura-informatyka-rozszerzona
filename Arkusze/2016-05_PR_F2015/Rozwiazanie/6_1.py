def szyfruj(slowo, k):
    wynik = ""

    for znak in slowo:
        wynik += chr((ord(znak) - 65 + k) % 26 + 65)

    return wynik

with open("dane_6_1.txt") as f, open("wyniki_6_1.txt", "w") as g:
    for slowo in f:
        g.write(szyfruj(slowo.strip(), 107) + "\n")