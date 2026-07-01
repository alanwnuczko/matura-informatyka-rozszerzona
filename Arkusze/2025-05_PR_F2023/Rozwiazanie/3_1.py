import math

def wartosc_bezwzgledna(n): # Zamiast własnej funkcji można użyć abs()
    if n == 0:
        return 0
    elif n > 0:
        return n
    else:
        return n * -1

licznik = 0

with open("dron.txt") as f:
    for line in f:
        line = line.strip().split(" ")

        A = int(line[0])
        B = int(line[1])
        A = wartosc_bezwzgledna(A) # A = abs(A)
        B = wartosc_bezwzgledna(B) # B = abs(B)

        if B == 0:
            NWD = A
            if NWD > 1:
                licznik += 1

        elif B > 0:
            NWD = math.gcd(A, B)
            if NWD > 1:
                licznik += 1

print(licznik)