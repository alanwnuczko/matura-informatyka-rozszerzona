numery_telefonow = []
with open("dane.txt") as f:
    napis = f.read()

    for i in range(len(napis) - 8):
        numer = napis[i:i+9]

        if numer.isdigit():
            przed = i == 0 or not napis[i-1].isdigit()
            po = i + 9 == len(napis) or not napis[i+9].isdigit()

            if przed and po:
                numery_telefonow.append(numer)

najmniej = 10
wynik = []

for numer in numery_telefonow:
    rozne_cyfry = []

    for cyfra in numer:
        if cyfra not in rozne_cyfry:
            rozne_cyfry.append(cyfra)

    if len(rozne_cyfry) < najmniej:
        najmniej = len(rozne_cyfry)
        wynik = [numer]

    elif len(rozne_cyfry) == najmniej:
        wynik.append(numer)


for wynik in wynik:
    print(wynik)