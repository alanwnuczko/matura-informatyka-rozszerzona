przesuniecia_A = []
przesuniecia_B = []
licznik_w_kwadracie = 0
with open("dron.txt") as f:
    for line in f:
        line = line.split()
        przesuniecia_A.append(int(line[0]))
        przesuniecia_B.append(int(line[1]))

    suma_A = 0
    lista_przesuniec_A = []
    for i in range(len(przesuniecia_A)):
        suma_A += przesuniecia_A[i]
        lista_przesuniec_A.append(suma_A)

    suma_B = 0
    lista_przesuniec_B = []
    for i in range(len(przesuniecia_B)):
        suma_B += przesuniecia_B[i]
        lista_przesuniec_B.append(suma_B)

    for i in range(len(lista_przesuniec_A)):
        x = lista_przesuniec_A[i]
        y = lista_przesuniec_B[i]

        if 0 < x < 5000 and 0 < y < 5000:
            licznik_w_kwadracie += 1

# a)
    print(licznik_w_kwadracie)

# b)
    punkty = list(zip(lista_przesuniec_A, lista_przesuniec_B))
    n = len(punkty)

    for i in range(n):
        x_B, y_B = punkty[i]

        for j in range(n):
            for k in range(j + 1, n):
                x_A, y_A = punkty[j]
                x_C, y_C = punkty[k]

                if x_B == (x_A + x_C) / 2 and y_B == (y_A + y_C) / 2:
                    print(punkty[j], punkty[i], punkty[k])