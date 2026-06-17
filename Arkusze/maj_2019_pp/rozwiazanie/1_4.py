def algorytm2(s):
    n = len(s)

    r = [''] * n
    k = 0
    for i in range(n - 1, -1, -1):
        r[k] = s[i]
        k += 1

    ile = 0
    for i in range(n):
        if r[i] == s[i]:
            ile += 1
        else:
            break

    if ile == n:
        ile = ile // 2

    p = [''] * n
    for i in range(ile):
        p[i] = s[i]
        p[i + ile] = s[n + i - ile]

    if ile == n // 2:
        print("napis s jest palindromem")

    return ile, p


print(algorytm2("abcba"))