def czy_pierwsza(n):
    if n < 2:
        return "NIE"

    for i in range(2, n):
        if n % i == 0:
            return "NIE"

    return "TAK"

print(czy_pierwsza(4))