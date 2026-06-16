def pisz(s, n, k):
    if len(s) == n:
        print(s)
    else:
        for i in range(k):
            pisz(s + str(i), n, k)

print(pisz("", 2, 3))