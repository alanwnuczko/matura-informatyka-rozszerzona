licznik = 0 # Do zadania 2_2
def algorytm(A):
    n = len(A)
    for i in range(n-1):
        m = i
        for j in range(i + 1, n):
            if A[m] < A[j]:
                m = j
        if i != m:
            A[i], A[m] = A[m], A[i]
            global licznik # Do zadania 2_2
            licznik += 1 # Do zadania 2_2
    return A

print(algorytm([1, 2, 3, 7, 8, 6, 7]))
print(licznik) # Do zadania 2_2