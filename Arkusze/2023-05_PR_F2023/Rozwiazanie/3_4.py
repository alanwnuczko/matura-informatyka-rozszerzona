cyfry = []
with open("pi.txt") as f:
    for line in f:
        cyfry.append(line.strip())

n = len(cyfry)

inc = [1] * n
for i in range(1, n):
    if int(cyfry[i]) > int(cyfry[i-1]):
        inc[i] = inc[i-1] + 1

dec = [1] * n
for i in range(n-2, -1, -1):
    if int(cyfry[i]) > int(cyfry[i+1]):
        dec[i] = dec[i+1] + 1

max_dlugosc = 0
najlepszy_start = -1

for i in range(n-1):
    if inc[i] >= 2 and dec[i+1] >= 2:
        dlugosc = inc[i] + dec[i + 1]
        if dlugosc > max_dlugosc:
            max_dlugosc = dlugosc
            najlepszy_start = i - inc[i] + 1

wiersz_startowy = najlepszy_start + 1
znalaziony_ciag = "".join(cyfry[najlepszy_start : najlepszy_start + max_dlugosc])

print(wiersz_startowy)
print(znalaziony_ciag)