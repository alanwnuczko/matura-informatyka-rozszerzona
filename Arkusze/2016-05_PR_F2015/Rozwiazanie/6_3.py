def klucz(slowo, szyfr):
    k = (ord(szyfr[0]) - ord(slowo[0])) % 26

    for i in range(1, len(slowo)):
        if (ord(szyfr[i]) - ord(slowo[i])) % 26 != k:
            return False

    return True

with open("dane_6_3.txt") as f, open("wyniki_6_3.txt", "w") as g:
    for line in f:
        slowo, szyfr = line.split()

        if not klucz(slowo, szyfr):
            g.write(slowo + "\n")