def wyszukiwanie_liniowe(T, x):
    for i in range(len(T)):
        if T[i] == x:
            return i

print(wyszukiwanie_liniowe([1, 3, 6 , 7, 12, 34, 56, 78], 56)) # Wynik 6 (indeks)