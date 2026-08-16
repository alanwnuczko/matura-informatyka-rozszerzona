with open("dane.txt") as f:
    napis = f.read().strip()

liczniki = {}
for i in range(0, len(napis), 2):
    para = napis[i:i+2]

    if para in liczniki:
        liczniki[para] += 1
    else:
        liczniki[para] = 1

posortowane = sorted(liczniki, key=lambda x: liczniki[x])

wynik = ""

for para in posortowane:
    wynik += para

print(wynik)
