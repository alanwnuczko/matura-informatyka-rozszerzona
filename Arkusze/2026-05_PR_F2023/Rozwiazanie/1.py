licznik = 0 # Do zadania 1_1
def A(m, n):
    global licznik # Do zadania 1_1

    if n == 1:
        return m
    elif n > 1 and n % 2 == 0:
        licznik += 1
        return A(2 * m, n / 2)
    elif n > 1 and n % 2 != 0:
        licznik += 1
        return 2 * A(m, (n-1) / 2) + m


print(A(2 * (10**6), 256 * (10**6)))
print(licznik) # Do zadania 1_1
print(512*(10**12)) # Do zadania 1_2
