def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

liczby_wynik = []
with open("liczby.txt") as f:
    for line in f:
        line = int(line)
        if czy_pierwsza(line) == True and line > 4000 and line < 5000:
            liczby_wynik.append(line)


print(liczby_wynik)
