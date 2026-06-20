def fun(a, b):
    if a <= 2:
        if a == 2:
            return True
        else:
            return False

    if a % b == 0:
        return False

    if b * b > a:
        return True

    return fun(a, b + 1)

# 2_1:
print(fun(0, 2))
print(fun(1, 2))
print(fun(7, 2))
print(fun(16, 2))
print(fun(-4, 2))


