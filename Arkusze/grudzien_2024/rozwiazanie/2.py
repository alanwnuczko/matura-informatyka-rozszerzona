licznik = 0

def F(x, p):
    global licznik
    licznik += 1

    if x == 0:
        return 0
    else:
        c = x % p
        if c % 2 == 1:
            return F(x // p, p) + c
        else:
            return F(x // p, p) - c

# Do zadania 2_1:
print(F(125, 2))
print(licznik)

# Do zadania 2_2:
# for i in range(1, 100):
#     global p
#     print(F(i, 3))
#
# for i in range(1, 100):
#     global p
#     print(F(i, 4))

