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
    if b == 0:
        return 0
    k = ostatnia(b)
    w = f(a, skroc(b))
    w = dopisz(w)

    while k > 0:
        w = w + a
        global licznik
        licznik += 1
        k = k - 1

    return w

# print(f(2024, 1000)) # a) 1
print(f(2024, 1234)) # b) 10
print(licznik)