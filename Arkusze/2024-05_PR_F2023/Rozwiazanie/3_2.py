def nieparzysty_skrot(n):
    m = 0
    potega = 1

    while n > 0:
        cyfra = n % 10

        if cyfra % 2 == 1:
            m = m + cyfra * potega
            potega *= 10

        n //= 10

    return m

licznik_brak_skrotow = 0
najwieksza_brak_skrotu = 0

with open("skrot.txt") as f:
    for line in f:
        liczba = int(line.strip())

        skrot = nieparzysty_skrot(liczba)
        if skrot == 0:
            licznik_brak_skrotow += 1

            if liczba > najwieksza_brak_skrotu:
                najwieksza_brak_skrotu = liczba

print(licznik_brak_skrotow)
print(najwieksza_brak_skrotu)