numery_telefonow = []
with open("dane.txt") as f:
    napis = f.read()

    for i in range(len(napis) - 8):
        if napis[i] == "5":
            numer = napis[i:i+9]

            if numer.isdigit():
                przed = i == 0 or not napis[i-1].isdigit()
                po = i + 9 == len(napis) or not napis[i+9].isdigit()

                if przed and po:
                    numery_telefonow.append(numer)

for numer_telefonu in numery_telefonow:
    print(numer_telefonu)
