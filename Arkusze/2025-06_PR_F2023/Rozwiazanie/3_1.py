with open("dane.txt") as f:
    napis = f.read()

    licznik = 0
    liczby = []

    i = 0
    while i < len(napis):
        if napis[i].isdigit():
            liczba = ""

            while i < len(napis) and napis[i].isdigit():
                liczba += napis[i]
                i += 1
            liczby.append(liczba)

        else:
            i += 1

for liczba in liczby:
    if liczba.startswith("50"):
        licznik += 1

print(licznik)