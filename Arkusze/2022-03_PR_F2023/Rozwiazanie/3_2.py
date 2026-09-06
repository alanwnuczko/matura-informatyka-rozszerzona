# Złożność O(x):
def algorytm1(a, x, M):
    b = (a ** x) % M
    return b

# Złożność O(log x):
def algorytm2(a, x, M):
    b = 1

    while x > 0:
        if x % 2 == 1:
            b = (b * a) % M

        a = (a * a) % M
        x //= 2

    return b