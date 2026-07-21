def czy_pierwsza(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

liczby_pierwsze = []

with open("dane_6.txt") as f:
    for line in f:
        liczba = int(line.strip())

        if czy_pierwsza(liczba):
            liczby_pierwsze.append(liczba)

print(min(liczby_pierwsze)) # Najmniejsza liczba
print(max(liczby_pierwsze)) # Największa liczba