def odszyfruj(s, k, n):
    s = list(s)
    i = ((len(s) - k - 1) // n) * n
    while i >= 0:
        s[i], s[i + k] = s[i + k], s[i]
        i -= n
    return "".join(s)

print(odszyfruj("eiindaezotinwezssyktpo", 2, 2)) # pieniadzetoniewszystko