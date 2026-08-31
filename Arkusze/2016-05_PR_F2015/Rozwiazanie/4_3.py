from math import pi

nk = 0
e = []

with open("punkty.txt") as f:
    for n, l in enumerate(f, 1):
        if n> 1700:
            break
        x, y = map(int, l.split())
        if (x - 200) ** 2 + (y - 200) ** 2 <= 40000:
            nk += 1
        e.append(abs(pi - 4 * nk / n))

print(round(e[999], 4))
print(round(e[1699], 4))