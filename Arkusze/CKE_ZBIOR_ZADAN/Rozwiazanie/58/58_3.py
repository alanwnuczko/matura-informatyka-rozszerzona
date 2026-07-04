temperatury_s1 = []
temperatury_s2 = []
temperatury_s3 = []
dni_rekordowe = 0
with open("dane_systemy1.txt") as s1, \
    open("dane_systemy2.txt") as s2, \
    open("dane_systemy3.txt") as s3:
        for line in s1:
            line = line.split()
            temperatury_s1.append(int(line[1], 2))

        for line in s2:
            line = line.split()
            temperatury_s2.append(int(line[1], 4))

        for line in s3:
            line = line.split()
            temperatury_s3.append(int(line[1], 8))

max_s1 = 0
max_s2 = 0
max_s3 = 0
for dzien in range(len(temperatury_s1)):
    if temperatury_s1[dzien] > max_s1:
        rekord_s1 = True
        max_s1 = temperatury_s1[dzien]
    else:
        rekord_s1 = False

    if temperatury_s2[dzien] > max_s2:
        rekord_s2 = True
        max_s2 = temperatury_s2[dzien]
    else:
        rekord_s2 = False

    if temperatury_s3[dzien] > max_s3:
        rekord_s3 = True
        max_s3 = temperatury_s3[dzien]
    else:
        rekord_s3 = False

    if rekord_s1 or rekord_s2 or rekord_s3:
        dni_rekordowe += 1

print(dni_rekordowe)
