def F(x, n):
    print(f"Wywołanie: F({x}, {n})")
    if n == 1:
        wynik = x
    else:
        if n % 3 == 0:
            k = F(x, n // 3)
            wynik = k * k * k
        else:
            wynik =  x * F(x, n - 1)

    print(f"Wynik F({x}, {n}) = {wynik}")
    return wynik

print(F(2, 10))


# wywołanie wynik
# F(2, 10)  1024
# F(2, 9)   512
# F(2, 3)   8
# F(2, 1)   2