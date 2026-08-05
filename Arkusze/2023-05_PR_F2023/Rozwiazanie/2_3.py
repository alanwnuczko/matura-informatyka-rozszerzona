liczby_dziesietne = []

with open("bin.txt") as f:
    for line in f:
        liczba = line.strip()
        liczby_dziesietne.append(int(liczba, 2))

print(bin(max(liczby_dziesietne))[2:])