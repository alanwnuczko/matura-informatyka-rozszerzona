liczby_wieksze_30 = []
suma_wszystkich = []
with open("liczby.txt") as f:
    for line in f:
        line = list(map(int, line.strip()))

        if sum(line) > 30:
            liczby_wieksze_30.append(line)

        suma_wszystkich.append(sum(line))
print(sum(suma_wszystkich))

for liczba in liczby_wieksze_30:
    liczba = int("".join(map(str, liczba)))
    # print(liczba)

