def czy_pierwsza(n): # Złożność obliczeniowa O(sqrt(n))
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True

max_liczba = 0
max_rozklady = -1

min_liczba = 0
min_rozklady = 10 ** 9

with open("liczby.txt") as f:
    for line in f:
        n = int(line)

        rozklady = 0

        for a in range(2, n // 2 + 1):
            b = n - a

            if czy_pierwsza(a) and czy_pierwsza(b):
                rozklady += 1

        if rozklady > max_rozklady:
            max_rozklady = rozklady
            max_liczba = n

        if rozklady < min_rozklady:
            min_rozklady = rozklady
            min_liczba = n

print(max_liczba, max_rozklady, min_liczba, min_rozklady)