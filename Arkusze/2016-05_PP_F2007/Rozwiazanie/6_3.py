def czy_pierwsza(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

wszystkie_liczby = []

with open("dane_6.txt") as f:
    for line in f:
        liczba = int(line.strip())
        wszystkie_liczby.append(liczba)

licznik = 0
for i in range(len(wszystkie_liczby) - 1):
    if (czy_pierwsza(wszystkie_liczby[i]) and czy_pierwsza(wszystkie_liczby[i+1]) and
        abs(wszystkie_liczby[i] - wszystkie_liczby[i+1]) == 2):
        licznik += 1

        print((wszystkie_liczby[i], wszystkie_liczby[i+1]))

print(licznik)