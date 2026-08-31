def suma_dzielnikow(n):
    suma = 1
    d = 2

    while d * d <= n:
        if n % d == 0:
            suma += d

            if d * d != n:
                suma += n // d

        d += 1

    return suma

def skojarzone(a):
    b = suma_dzielnikow(a) - 1

    if b > 1 and suma_dzielnikow(b) == a + 1:
        return b

    return "NIE"

print(skojarzone(140))