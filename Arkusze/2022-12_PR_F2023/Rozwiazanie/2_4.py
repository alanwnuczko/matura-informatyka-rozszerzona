# def rysuj(n):
#     if n < N:
#         rysuj(2 * n)
#         rysuj(2 * n + 1)

with open("pary.txt") as f:
    for line in f:
        x, y = map(int, line.split())

        temp = y

        while temp > x:
            temp //= 2

        if temp == x:
            print(x, y)