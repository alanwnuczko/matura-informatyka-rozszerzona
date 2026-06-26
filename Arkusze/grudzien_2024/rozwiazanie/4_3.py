lista_wysokosci = []
lista_szerokosci = []
with open("prostokaty.txt") as f:
    for line in f:
        parametry_prostokata = "".join(list(line))
        h = int(parametry_prostokata.split()[0])
        s = int(parametry_prostokata.split()[1])

        lista_wysokosci.append(h)
        lista_szerokosci.append(s)


wynik_2 = 0
wynik_3 = 0
wynik_5 = 0

for i in range(len(lista_wysokosci)):
    h = lista_wysokosci[i]
    szerokosci = []

    for j in range(len(lista_wysokosci)):
        if lista_wysokosci[j] == h:
            szerokosci.append(lista_szerokosci[j])

    szerokosci.sort(reverse = True)

    if len(szerokosci) >= 2:
        wynik_2 = max(wynik_2, szerokosci[0] + szerokosci[1])

    if len(szerokosci) >= 3:
        wynik_3 = max(wynik_3, szerokosci[0] + szerokosci[1] + szerokosci[2])

    if len(szerokosci) >= 5:
        wynik_5 = max(wynik_5, szerokosci[0] + szerokosci[1] + szerokosci[2] + szerokosci[3] + szerokosci[4])

print(f"2 prostokąty: {wynik_2}")
print(f"3 prostokąty: {wynik_3}")
print(f"5 prostokątów: {wynik_5}")