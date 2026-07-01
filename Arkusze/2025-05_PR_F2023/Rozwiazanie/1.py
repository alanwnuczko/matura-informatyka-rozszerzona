def przestaw(n):
    r = n % 100
    a = r // 10
    b = r % 10
    n = n // 100
    # global licznik
    # licznik = 1 - Liczy liczbę wywołań funkcji przestaw(n)

    if n > 0:
        w = a + 10 * b + 100 * przestaw(n)
        # licznik += 1
    else:
        if a > 0:
            w = a + 10 * b
        else:
            w = b
    return w

print(przestaw(316498))
# print(licznik)