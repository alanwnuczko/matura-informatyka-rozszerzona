miasta = []
with open("mapa.txt") as f:
    for line in f:
        line = line.strip().split()
        miasta.append(line)

najwiekszy_bok = 0
najwieksza_ludnosc = 0

for bok in range(1, 251):
    suma = 0

    for i in range(len(miasta)):
        x = int(miasta[i][0])
        y = int(miasta[i][1])
        populacja = int(miasta[i][2])

        if x > 0 and x < bok and y > 0 and y < bok:
            suma += populacja

    gestosc = suma / (bok * bok)

    if gestosc > 2:
        najwiekszy_bok = bok
        najwieksza_ludnosc = suma

print(najwiekszy_bok, najwieksza_ludnosc)