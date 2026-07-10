def przeniesienia(a, b):
    liczba_przeniesien = 0
    przeniesienie = 0

    while a > 0:
        suma = a % 10 + b % 10 + przeniesienie

        if suma >= 10:
            liczba_przeniesien += 1
            przeniesienie = 1
        else:
            przeniesienie = 0

        a //= 10
        b //= 10

    return liczba_przeniesien


print(przeniesienia(37932, 12528))