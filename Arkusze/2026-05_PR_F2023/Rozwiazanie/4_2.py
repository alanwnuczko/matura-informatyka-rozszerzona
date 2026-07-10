with open("korpo.txt") as f:
    szefowie = []

    for line in f:
        szefowie.append(int(line))

licznik = 0

for pracownik in range(len(szefowie) + 1):
    if pracownik not in szefowie:
        licznik += 1

print(licznik)