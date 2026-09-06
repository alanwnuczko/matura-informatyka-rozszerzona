def algorytm(a, x, M):
    b = (a ** x) % M
    return b

print(algorytm(5, 2, 31))