def czy_pierwsza(n): # Złożność obliczeniowa O(n)
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

licznik = 0

with open("liczby.txt") as f:
    for line in f:
        liczba = int(line)

        if czy_pierwsza(liczba - 1):
            licznik += 1

print(licznik)