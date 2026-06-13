# Elementy listy są trymane wewnątrz nawiasów kwadratowych
# Elementy listy są indeksowane - pierwszy element listy ma indeks 0

owoce = ["Jabłko", "Pomarańcza", "Winogrona"]

print(owoce) # Wynik: ['Jabłko', 'Pomarańcza', 'Winogrona']
print(owoce[0]) # Wynik: Jabłko
print(owoce[2]) # Wynik: Winogrona
print(owoce[-1]) # Wynik: Winogrona (ostatni element)
print(owoce[-2]) # Wynik: Pomarańcza (przedostatni element)

# Dodanie elementu do listy
owoce.append("Mango")
print(owoce) # Wynik: ['Jabłko', 'Pomarańcza', 'Winogrona', 'Mango']

# Zamiana elementów na podstawie indeksów
owoce[2] = "Kiwi" # Zamienia Winogrona na Kiwi
print(owoce) # Wynik: ['Jabłko', 'Pomarańcza', 'Kiwi']

# Usuwanie elementów listy
lista_bez_mango = owoce.pop() # Usuwa ostatni element listy
print(lista_bez_mango) # Wynik: Mango
print(owoce) # Wynik: ['Jabłko', 'Pomarańcza', 'Kiwi']

owoce.remove("Kiwi") # Usuwa "Kiwi z listy"
print(owoce) # Wynik: ['Jabłko', 'Pomarańcza']

oceny = [1, 2, 3, 4, 5, 6]
oceny_ucznia = [1, 5, 4, 2]


# Funkcje
print(len(owoce)) # len() zwraca liczbę elementów listy
print(sum(oceny)) # sum() zwraca sumę liczbowych elementow listy
print(min(oceny)) # min() zwraca najmniejszy liczbowy element listy
print(max(oceny)) # max() zwraca największy liczbowy element listy
print(sorted(oceny_ucznia)) # sorted() zwraca posortowaną listę
print(sorted(owoce)) # sorted() zwraca posortowaną alfabetycznie listę