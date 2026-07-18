def szyfruj(s, k, n):
    d = len(s)
    szyfr = list(s)

    i = 0
    while i + k < d:
        szyfr[i], szyfr[i + k] = szyfr[i + k], szyfr[i]
        i += n

    return "".join(szyfr)

print(szyfruj("ataknadranem", 4, 2)) # ntdkaaeranam
print(szyfruj("maturazinformatyki", 3, 5)) # uatmrnziafarmotyki
print(szyfruj("stokrotka", 1, 2)) # tskoorkta