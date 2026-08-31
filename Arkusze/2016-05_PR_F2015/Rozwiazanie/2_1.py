def przestaw(A):
    n = len(A)
    klucz = A[0]
    w = 1

    for k in range(1, n):
        if A[k] < klucz:
            A[w], A[k] = A[k], A[w]
            w += 1

    return A

print(przestaw([4, 6, 3, 5, 2, 1]))