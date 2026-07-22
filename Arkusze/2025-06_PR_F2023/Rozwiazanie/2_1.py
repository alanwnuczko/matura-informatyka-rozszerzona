def liczba_cyfr(n):
    cyfry = 0
    while n > 0:
        cyfry += 1
        n //= 10
    return cyfry

def przeciecie(k):
    cyfry = liczba_cyfr(k)
    p = 1
    i = 0
    while i < cyfry // 2:
        p *= 10
        i += 1

    a = k // p
    b = k % p

    return a, b

print(przeciecie(123456))