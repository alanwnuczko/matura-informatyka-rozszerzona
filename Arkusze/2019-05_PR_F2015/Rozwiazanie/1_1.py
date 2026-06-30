# Złożność liniowa:
def pierwsza_liczba_jasia(A):
    for i in A:
        if i % 2 == 0:
            return i

A = [5, 99, 3, 7, 111, 13, 4, 24, 4, 8]
print(pierwsza_liczba_jasia(A))


# Wyszukiwanie binarne:
def pierwsza_liczba_jasia(A):
    lewy = 0
    prawy = len(A) - 1

    while lewy < prawy:
        s = (lewy + prawy) // 2

        if A[s] % 2 == 0:
            prawy = s
        else:
            lewy = s + 1

    return A[lewy]

A = [5, 99, 3, 7, 111, 13, 4, 24, 4, 8]
print(pierwsza_liczba_jasia(A))