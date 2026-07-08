def sortowanie_babelkowe(T):
    n = len(T)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if T[j] > T[j + 1]:
                T[j], T[j + 1] = T[j + 1], T[j]
    return T

print(sortowanie_babelkowe([4, 2, 7, 11, 3, 2, 9, 1]))