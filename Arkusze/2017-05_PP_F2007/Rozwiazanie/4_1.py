licznik = 0

with open("liczby.txt") as f:
    for line in f:
        liczby = list(map(int, line.strip().split()))

        if liczby[0] < liczby[1] < liczby[2]:
            licznik += 1

print(licznik)