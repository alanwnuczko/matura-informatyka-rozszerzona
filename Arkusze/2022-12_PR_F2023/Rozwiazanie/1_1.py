licznik = 0
with open("mecz.txt") as f:
    for znaki in f:
        znaki = znaki.strip()

        for i in range(len(znaki) - 1):
            if znaki[i] != znaki[i+1]:
                licznik += 1

print(licznik)
