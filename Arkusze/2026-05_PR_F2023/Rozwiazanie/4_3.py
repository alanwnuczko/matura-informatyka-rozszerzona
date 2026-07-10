with open("korpo.txt") as f:
    szefowie = []

    for line in f:
        szefowie.append(int(line))

ma_najwiecej = 0
maks_podwladnych = 0

for i in range(1, len(szefowie) + 1):
    licznik = 0

    for j in szefowie:
        if j == i:
            licznik += 1

    if licznik > maks_podwladnych:
        maks_podwladnych = licznik

        ma_najwiecej = i

print(ma_najwiecej, maks_podwladnych)
