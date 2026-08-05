cyfry = []
with open("pi.txt") as f:
    for line in f:
        cyfry.append(int(line.strip()))

def czy_rosnaco_malejacy(c):
    for k in range(2, 5):
        pierwszy = c[:k]
        drugi = c[k:]

        rosnacy = all(pierwszy[j] < pierwszy[j+1] for j in range(len(pierwszy) - 1))
        malejacy = all(drugi[j] > drugi[j+1] for j in range(len(drugi) - 1))

        if rosnacy and malejacy:
            return True

    return False

licznik = 0
for i in range(len(cyfry) - 5):
    ciag_6 = cyfry[i : i+6]
    if czy_rosnaco_malejacy(ciag_6):
        licznik += 1

print(licznik)