licznik_nieparzystych = 0
with open("liczby.txt") as f:
    for line in f:
        if int(line) % 2 != 0:
            licznik_nieparzystych += 1

print(licznik_nieparzystych)