def przestaw2(n):
    w = 0
    p = 1
    while n > 0:
        r = n % 100
        a = r // 10
        b = r % 10

        if n > 9:
            w = p * a + 10 * p * b + w
        else:
            w = p * b + w
        n = n // 100
        p = p * 100
    return w

print(przestaw2(21))