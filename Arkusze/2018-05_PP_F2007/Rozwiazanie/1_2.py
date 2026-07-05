def odszyfrowanie(S):
    S = list(S)
    n = len(S)
    if n % 2 == 0:
        for i in range(0, n-1, 2):
            S[i], S[i+1] = S[i+1], S[i]
    else:
        S[0], S[n - 1] = S[n - 1], S[0]
        for i in range(0, n-1, 2):
            S[i], S[i+1] = S[i+1], S[i]

    return "".join(S)
print(odszyfrowanie("AGAIDZW"))