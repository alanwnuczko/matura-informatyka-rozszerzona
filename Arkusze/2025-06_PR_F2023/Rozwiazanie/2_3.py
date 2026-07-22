def stopien_kaprekara(n):
    kwadrat = str(n * n)
    licznik = 0

    for i in range(1, len(kwadrat)):
        a = int(kwadrat[:i])
        b = int(kwadrat[i:])

        if a + b <= n:
            licznik += 1

    return licznik

with open("liczby2.txt") as f:
    stopnie_kaprekara = []
    liczby = []

    for line in f:
        liczba = int(line.strip())

        stopnie_kaprekara.append(stopien_kaprekara(liczba))
        liczby.append(liczba)

najwiekszy_stopien = max(stopnie_kaprekara)
indeks = stopnie_kaprekara.index(najwiekszy_stopien)

print(najwiekszy_stopien)
print(liczby[indeks])