def czy_pierwsza(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

liczba_pierwszych_M = 0

with open("liczby.txt") as f:
    for line in f:
        M, a, b = map(int, line.split())

        if czy_pierwsza(M):
            liczba_pierwszych_M += 1

print(liczba_pierwszych_M)