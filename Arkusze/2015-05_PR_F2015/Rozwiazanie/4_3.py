liczby = []
with open("liczby.txt") as f:
    for line in f:
        liczba = int(line.strip(), 2)
        liczby.append(liczba)

print(liczby.index(min(liczby)) + 1) # Wynik: 859
print(liczby.index(max(liczby)) + 1) # Wynik: 925