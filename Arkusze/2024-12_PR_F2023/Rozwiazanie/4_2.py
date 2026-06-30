lista_wysokosci = []
lista_szerokosci = []
with open("prostokaty.txt") as f:
    for line in f:
        parametry_prostokata = "".join(list(line))
        h = int(parametry_prostokata.split()[0])
        s = int(parametry_prostokata.split()[1])

        lista_wysokosci.append(h)
        lista_szerokosci.append(s)

    licznik_ciagu = 1
    najdluzszy_ciag = 1

    ostatnia_h = lista_wysokosci[0]
    ostatnia_s = lista_szerokosci[0]
    for i in range(0, len(lista_wysokosci) - 1):
        if lista_wysokosci[i] >= lista_wysokosci[i+1] and lista_szerokosci[i] >= lista_szerokosci[i+1]:
            licznik_ciagu += 1

            if licznik_ciagu > najdluzszy_ciag:
                najdluzszy_ciag = licznik_ciagu
                ostatnia_h = lista_wysokosci[i + 1]
                ostatnia_s = lista_szerokosci[i + 1]
        else:
            licznik_ciagu = 1


print(najdluzszy_ciag, ostatnia_h, ostatnia_s)


