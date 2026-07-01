with open("symbole.txt") as f:
    tab = [list(line.strip()) for line in f]

licznik = 0

for i in range(1, len(tab) - 1):
    for j in range(1, len(tab[0]) - 1):
        znak = tab[i][j]

        if(
                tab[i - 1][j - 1] == znak and
                tab[i - 1][j] == znak and
                tab[i - 1][j + 1] == znak and
                tab[i][j - 1] == znak and
                tab[i][j] == znak and
                tab[i][j + 1] == znak and
                tab[i + 1][j - 1] == znak and
                tab[i + 1][j] == znak and
                tab[i + 1][j + 1] == znak
        ):
            licznik += 1
            print(i + 1, j+ 1)
print(licznik)