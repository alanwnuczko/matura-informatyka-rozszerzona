temperatury_S1 = []
temperatury_S1_int = []
with open("dane_systemy1.txt") as s1:
    for line in s1:
        line = line.strip().split()
        temperatury_S1.append(line[1])
for temperatura in temperatury_S1:
    temperatury_S1_int.append(int(temperatura, 2))
print(bin(min(temperatury_S1_int)))

temperatury_S2 = []
temperatury_S2_int = []
with open("dane_systemy2.txt") as s2:
    for line in s2:
        line = line.strip().split()
        temperatury_S2.append(line[1])
for temperatura in temperatury_S2:
    temperatury_S2_int.append(int(temperatura, 4))
print(bin(min(temperatury_S2_int)))

temperatury_S3 = []
temperatury_S3_int = []
with open("dane_systemy3.txt") as s3:
    for line in s3:
        line = line.strip().split()
        temperatury_S3.append(line[1])
for temperatura in temperatury_S3:
    temperatury_S3_int.append(int(temperatura, 8))
print(bin(min(temperatury_S3_int)))