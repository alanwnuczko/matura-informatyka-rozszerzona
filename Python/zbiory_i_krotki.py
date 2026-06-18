# Krotki - Są jak listy ale nie można zmieniać ich wartości po jej utworzeniu
krotka = (32, 64)
print(krotka[0]) # Wynik: 32

# Zbiory - Kolekcja nieuporządkowanych i niepowtarzalnych elementów
A = {1, 2, 3, 4,}
B = {3, 4, 5, 6}

# Operacje na zbiorach:
print(A | B) # Drukuje wszystkie elementy z obu zbiorów. Wynik: {1, 2, 3, 4, 5, 6}
print(A & B) # Drukuje część wspólną. Wynik: {3, 4}
print(A - B) # Różnica w A. Wynik: {1, 2}
print(B - A) # Różnica w B. Wynik: {5, 6}
print(A ^ B) # Różnica symetryczna. Wynik: {1, 2, 5, 6}

# Przykłady

# Zadanie 1
#Masz krotke:
dane = ("Ala", 12, 4.5, True)

# Wypisz:
# Pierwszy element
print(dane[0])

# Ostatni element
print(dane[-1])

# Długosc krotki
print(len(dane))


# Zadanie 2
# Masz krotke:
punkt = (3, 7)

# Przypisz wartości do zmiennych x i y
x, y = punkt
print(punkt)


#Zadanie 3
# Utwórz słownik, w którym kluczem będzie krotka współrzędnych (x, y), a wartością nazwa punktu
punkty = {
    (0, 0): "Początek",
    (1, 2): "A",
    (3, 4): "B"
}

print(punkty[(3,4)])

# Zadanie 4
# Masz listę:
lista = [1, 2, 2, 3, 4, 4, 4, 5]

# Usuń duplikaty
unikalne = list(set(lista))
print(unikalne)


# Zadanie 5
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Wyznacz:
# Sumę zbiorów
print (A | B)

# Część wspólna
print(A & B)

# Różnicę A-B
print(A - B)


# Zadanie 6
tekst = "programowanie"

# Sprawdź, ile unikalnych liter zawiera
unikalne = set(tekst)
print(len(unikalne))


# Zadanie 7
# Masz dwie listy:
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7]

# Znajdź:
# Elementy wspólne
wspolne = list(set(l1) & set(l2))
print(wspolne)

# Elementy tylko w l1
result1 = [item for item in l1 if item not in l2]
print(result1)

# Elementy tylko w l2
result2 = [item for item in l2 if item not in l1]
print(result2)


# Zadanie 8
# Masz krotke:
k = (10, 20, 30, 40)

# Wypisz:
# Pierwszy Element
print(k[0])

# Drugi Element
print(k[1])

# Długosc krotki
print(len(k))


# Zadanie 9
# Masz listę:
lista = [1, 1, 2, 3, 3, 3, 4]

# Usuń duplikaty
unikalne = list(set(lista))
print(unikalne)