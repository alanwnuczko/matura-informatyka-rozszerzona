miasta = []
with open("mapa.txt") as f:
    for line in f:
        line = line.strip().split()
        miasta.append(line)

najwieksza = 0
numer = 0

for i in range(len(miasta)):
    populacja = int(miasta[i][2])

    if populacja > najwieksza:
        najwieksza = populacja
        numer = i + 1

print(numer, najwieksza)