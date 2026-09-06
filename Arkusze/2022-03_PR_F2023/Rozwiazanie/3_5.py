def potega(a, x, M):
    b = 1

    while x > 0:
        if x % 2 == 1:
            b = (b * a) % M

        a = (a * a) % M
        x //= 2

    return b

licznik = 0

with open("liczby.txt") as f:
    for line in f:
        M, a, b = map(int, line.split())

        for x in range(0, M):
            if potega(a, x, M) == b:
                licznik += 1
                break

print(licznik)