def nieparzysty_skrot(n):
    m = 0
    potega = 1

    while n > 0:
        cyfra = n % 10

        if cyfra % 2 == 1:
            m = m + cyfra * potega
            potega *=10

        n //= 10
    return m

from math import gcd
wynik = []
with open("skrot2.txt") as f:
    for line in f:
        liczba = int(line.strip())
        skrot = nieparzysty_skrot(liczba)

        if gcd(liczba, skrot) == 7:
            wynik.append(liczba)

for i in wynik:
    print(i)