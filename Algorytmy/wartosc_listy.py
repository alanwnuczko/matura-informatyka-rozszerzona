# Najmniejszą wartość z listy:

lista1 = [34, 65, 12, 21, 101, 362, 9, 365]

najmniejsza_wartosc = lista1[0]

for i in lista1:
    if i < najmniejsza_wartosc:
        najmniejsza_wartosc = i

print(f"Najmniejsza wartość: {najmniejsza_wartosc}")


# Największa:

lista2 = [34, 65, 12, 21, 101, 362, 9, 365]

najwieksza_wartosc = lista2[0]

for i in lista2:
    if i > najwieksza_wartosc:
        najwieksza_wartosc = i

print(f"Największa wartość: {najwieksza_wartosc}")
