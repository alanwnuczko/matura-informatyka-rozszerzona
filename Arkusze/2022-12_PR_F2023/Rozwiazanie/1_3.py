licznik_pass = 0
najdluzsza = 0
druzyna_naj = ""

with open("mecz.txt") as f:
    znaki = list(f.readline().strip())

    for i in range(len(znaki)):
        if i > 0 and znaki[i] == znaki[i-1]:
            continue

        licznik = 1

        for j in range(i + 1, len(znaki)):
            if znaki[i] == znaki[j]:
                licznik += 1
            else:
                break

        if licznik >= 10:
            licznik_pass += 1

            if licznik > najdluzsza:
                najdluzsza = licznik
                druzyna_naj = znaki[i]

print(licznik_pass, druzyna_naj, najdluzsza)