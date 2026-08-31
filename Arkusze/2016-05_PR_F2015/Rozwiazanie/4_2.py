with open("punkty.txt") as f:
    punkty = []

    for line in f:
        x, y = map(int, line.split())
        punkty.append((x, y))

for n in [1000, 5000, 10000]:
    nk = 0

    for x, y in punkty[:n]:
        if (x - 200) ** 2 + (y - 200) ** 2 <= 200 ** 2:
            nk += 1

    pi = 4 * nk / n

    print(n, round(pi, 4))