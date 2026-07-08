licznik_mniejsze_1000 = 0
liczby_mniejsze_1000 = []

with open("liczby.txt") as f:
    for line in f:
        line= int(line.strip())
        if line < 1000:
            licznik_mniejsze_1000 += 1
            liczby_mniejsze_1000.append(line)

print(licznik_mniejsze_1000)
print(liczby_mniejsze_1000[(len(liczby_mniejsze_1000)-2):])
