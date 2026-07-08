def wyszukiwanie_binarne(T, x):
    left = 0
    right = len(T) - 1

    while left <= right:
        center = (left + right) // 2

        if T[center] == x:
            return center

        elif T[center] < x:
            left = center + 1

        else:
            right = center - 1

print(wyszukiwanie_binarne([1, 4, 6, 7, 9, 19, 34, 78, 344, 567, 899, 900, 1001, 1232], 1001)) # Wynik: 12 (indeks)