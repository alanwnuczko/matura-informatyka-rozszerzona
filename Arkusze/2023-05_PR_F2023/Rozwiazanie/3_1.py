liczby = []
with open("pi.txt") as f:
    for line in f:
        liczba = line.strip()
        liczby.append(liczba)

licznik = 0

for i in range(len(liczby) - 1):
    fragment = int(liczby[i] + liczby[i+1])

    if fragment > 90:
        licznik += 1

print(licznik)