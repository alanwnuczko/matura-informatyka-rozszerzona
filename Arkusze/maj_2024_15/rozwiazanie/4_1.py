plansza = []

with open("plansza.txt") as f:
    for linia in f:
        plansza.append(list(map(int, linia.split())))

n = 100
licznik = 0

for i in range(n):
    for j in range(n):
        if plansza[i][j] == 0:

            mozna = True

            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue

                    ni = i + di
                    nj = j + dj

                    if 0 <= ni < n and 0 <= nj < n:
                        if plansza[ni][nj] == 1:
                            mozna = False

            if mozna:
                licznik += 1

print(licznik)