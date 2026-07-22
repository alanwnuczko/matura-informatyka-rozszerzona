def skroc(x):
    if x < 10:
        return 0
    return x // 10

def dopisz(x):
    return x * 10

def ostatnia(x):
    return x % 10

def f(a, b):
    if b == 0:
        return 0
    k = ostatnia(b)
    w = f(a, skroc(b))
    w = dopisz(w)

    while k > 0:
        w = w + a
        k = k - 1

    return w

print(f(42, 2)) # Wynik: 84
print(f(4, 125)) # Wynik: 500
print(f(103, 104)) # Wynik: 10712
