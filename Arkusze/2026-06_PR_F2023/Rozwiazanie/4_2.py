miasta = []
with open("mapa.txt") as f:
    for line in f:
        line = line.strip().split()
        miasta.append(line)

najmniejsza = 5000

for i in range(len(miasta)):
    for j in range(i + 1, len(miasta)):
        x1 = int(miasta[i][0])
        y1 = int(miasta[i][1])
        x2 = int(miasta[j][0])
        y2 = int(miasta[j][1])

        odleglosc = abs(x1 - x2) + abs(y1 - y2)

        if odleglosc < najmniejsza:
            najmniejsza = odleglosc

print(najmniejsza)

for i in range(len(miasta)):
    for j in range(i+1, len(miasta)):
        x1 = int(miasta[i][0])
        y1 = int(miasta[i][1])
        x2 = int(miasta[j][0])
        y2 = int(miasta[j][1])

        odleglosc = abs(x1 - x2) + abs(y1 - y2)

        if odleglosc == najmniejsza:
            print(i + 1, j + 1)