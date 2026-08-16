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

print(Szyfr("defragmentacja", 15)) # Wynik: ajcatnemgarfed
print(Szyfr("defragmentacja", 16)) # Wynik: ajcatnemgarfed
print(Szyfr("defragmentacja", 17)) # Wynik: ajcatnemgarfed

# Odp: k > n