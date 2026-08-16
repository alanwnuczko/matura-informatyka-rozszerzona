def Szyfr(T, k):
    n = len(T)
    S = [""] * n

    a = n // k
    c = n - a
    for i in range(1, n+1):
        if i % k == 0:
            b = i // k
            S[n - a + b - 1] = T[i - 1]
        else:
            S[c - 1] = T[i - 1]
            c -= 1

    return "".join(S)

print(Szyfr("defragmentacja", 1)) # Wynik: defragmentacja
print(Szyfr("tropikalny", 1)) # Wynik: tropikalny

# Podaj wartość klucza k, dla której zawsze szyfrogram i tekst jawny są identyczne: k = 1