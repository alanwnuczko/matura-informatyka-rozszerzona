licznik_35 = 0
sumy_liczb = []
liczba_wierszy_najwieksza_suma = 0

with open("liczby.txt") as f:
    for line in f:
        trojki_liczb = line.split()

        cyfry = [int(cyfra) for liczba in trojki_liczb for cyfra in liczba]

        if sum(cyfry) == 35:
            licznik_35 += 1

        sumy_liczb.append(sum(cyfry))

    for suma in sumy_liczb:
        if suma == max(sumy_liczb):
            liczba_wierszy_najwieksza_suma += 1

print(licznik_35)
print(max(sumy_liczb))
print(liczba_wierszy_najwieksza_suma)