def F(x, n):
    if n == 1:
        return x
    else:
        if n % 3 == 0:
            k = F(x, n // 3)
            return k * k * k
        else:
            return x * F(x, n - 1)

print(F(4, 9))