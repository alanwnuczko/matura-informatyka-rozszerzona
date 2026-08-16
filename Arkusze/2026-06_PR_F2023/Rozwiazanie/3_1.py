with open("dane.txt") as f:
    napis = f.readline().strip()

wynik = 0

for i in range(0, len(napis) - 2, 2):
    if napis[i:i+2] == napis[i+2:i+4]:
        wynik += 1

print(wynik)