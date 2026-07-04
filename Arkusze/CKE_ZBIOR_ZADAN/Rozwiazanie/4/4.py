import math

def na_silniowy(n):
    i = 1
    while math.factorial(i) <= n:
        i += 1

    i -= 1
    wynik = []

    while i > 0:
        f = math.factorial(i)
        wynik.append(str(n // f))
        n = n % f
        i -= 1

    return int("".join(wynik))

print(na_silniowy(5489))