def algorytm(a, n, T):
    T = [0] + T
    s = 0
    i = 1
    while i <= n:
        if T[i] == a:
            while i < n:
                i += 1
                s = s + T[i]
        i += 1
    return i, s

# 1_1:
print(algorytm(6, 9, [1, 5, 4, 2, 6, 3, 2, 7, 3]))

# 1_2:
# Jeśli liczba a jest w tablicy - to s jest równie sumie elementów po liczbie a w tablicy

# 1_3:
print(algorytm(9, 10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 2019]))