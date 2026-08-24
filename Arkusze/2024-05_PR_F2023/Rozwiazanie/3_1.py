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

print(nieparzysty_skrot(294762))