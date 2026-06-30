lista_pola = []
with open("prostokaty.txt") as f:
    for line in f:
        parametry_prostokata = "".join(list(line))
        h = int(parametry_prostokata.split()[0])
        s = int(parametry_prostokata.split()[1])

        pole_powierzchni = h * s

        lista_pola.append(pole_powierzchni)
    print(f"Najmniejsze pole: {min(lista_pola)}")
    print(f"Największe pole: {max(lista_pola)}")