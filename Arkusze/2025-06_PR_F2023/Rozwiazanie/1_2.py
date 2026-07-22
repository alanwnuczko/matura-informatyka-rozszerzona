def skroc(x):
    if x < 10:
        return 0
    return x // 10

def dopisz(x):
    return x * 10

def ostatnia(x):
    return x % 10

licznik = 0
def f(a, b):
    global licznik
    licznik += 1

    if b == 0:
        return 0
    k = ostatnia(b)
    w = f(a, skroc(b))
    w = dopisz(w)

    while k > 0:
        w = w + a
        k = k - 1

    return w

print(f(987654321, 123456789))
print(licznik) # Wynik: 10