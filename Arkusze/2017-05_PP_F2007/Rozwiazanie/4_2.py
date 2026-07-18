import math
najwieksze_wspolne_dzielniki = []

with open("liczby.txt") as f:
    for line in f:
        trojki_liczb = list(map(int, line.strip().split()))

        najwieksze_wspolne_dzielniki.append(math.gcd(*trojki_liczb))

print(sum(najwieksze_wspolne_dzielniki))