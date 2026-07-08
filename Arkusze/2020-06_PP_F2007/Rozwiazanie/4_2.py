liczby_wynik = []
with open("liczby.txt") as f:
    for line in f:
        line = line.strip()
        cyfry = list(line)
        for i in range(len(cyfry)):
            cyfry[i] = int(cyfry[i])
        if sum(cyfry) == 11:
            liczby_wynik.append(int(line))

print(liczby_wynik)