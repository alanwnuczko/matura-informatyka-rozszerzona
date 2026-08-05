def liczba_blokow(n):
    b = 1
    poprzedni = n % 2
    n //= 2

    while n > 0:
        obecny = n % 2
        if obecny != poprzedni:
            b += 1
        poprzedni = obecny
        n //= 2

    return b


print(liczba_blokow(67))
print(liczba_blokow(245))