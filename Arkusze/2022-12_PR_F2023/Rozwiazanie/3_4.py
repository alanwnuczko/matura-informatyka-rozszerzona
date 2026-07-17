liczniki = {}

for cyfra in "0123456789ABCDEF":
    liczniki[cyfra] = 0

with open("liczby.txt") as f:
    for line in f:
        liczba_hex = hex(int(line))[2:].upper()

        for znak in liczba_hex:
            liczniki[znak] += 1

for cyfra in "0123456789ABCDEF":
    print(cyfra + ":" + str(liczniki[cyfra]))