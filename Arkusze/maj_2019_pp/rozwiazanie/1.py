def algorytm1(s):
    ile = 0
    k = 0
    n = len(s)

    r = [''] * n

    for i in range(n - 1, -1, -1):
        r[k] = s[i]
        k += 1

    for i in range(n):
        if r[i] != s[i]:
            ile += 1
    return ile

print(algorytm1("aaaaabaaaaa"))