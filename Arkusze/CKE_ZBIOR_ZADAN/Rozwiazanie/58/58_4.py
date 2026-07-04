import math

temperatury_s1 = []

with open("dane_systemy1.txt") as s1:
    for line in s1:
        line = line.split()
        temperatury_s1.append(int(line[1], 2))

max_skok = 0

n = len(temperatury_s1)

for i in range(n):
    for j in range(i + 1, n):
        diff = temperatury_s1[i] - temperatury_s1[j]
        rij = diff * diff
        skok = math.ceil(rij / abs(i - j))
        if skok > max_skok:
            max_skok = skok

print(max_skok)