stany_zegara_s1 = []
licznik_niepoprawnych_s1 = 0
with open("dane_systemy1.txt") as s1:
    for line in s1:
        line = line.split()
        stany_zegara_s1.append(int(line[0], 2))
    for i in range(len(stany_zegara_s1)):
        oczekiwany = 12 + 24 * i
        if stany_zegara_s1[i] != oczekiwany:
            licznik_niepoprawnych_s1 += 1

stany_zegara_s2 = []
licznik_niepoprawnych_s2 = 0
with open("dane_systemy2.txt") as s2:
    for line in s2:
        line = line.split()
        stany_zegara_s2.append(int(line[0], 4))
    for i in range(len(stany_zegara_s2)):
        oczekiwany = 12 + 24 * i
        if stany_zegara_s2[i] != oczekiwany:
            licznik_niepoprawnych_s2 += 1

stany_zegara_s3 = []
licznik_niepoprawnych_s3 = 0
with open("dane_systemy3.txt") as s3:
    for line in s3:
        line = line.split()
        stany_zegara_s3.append(int(line[0], 8))
    for i in range(len(stany_zegara_s3)):
        oczekiwany = 12 + 24 * i
        if stany_zegara_s3[i] != oczekiwany:
            licznik_niepoprawnych_s3 += 1

licznik_wszystkie_bledne = 0
for j in range(len(stany_zegara_s1)):
    oczekiwany = 12 + 24 * j
    if stany_zegara_s1[j] != oczekiwany and stany_zegara_s2[j] != oczekiwany and stany_zegara_s3[j] != oczekiwany:
        licznik_wszystkie_bledne += 1

print(licznik_wszystkie_bledne)