def na_trojkowy(n):
    wynik = ""

    if n == 0:
        return "0"
    while n > 0:
        wynik = str(n % 3) + wynik
        n = n // 3
    return wynik

# znak o odpowiada cyfrze 0
# znak + odpowiada cyfrze 1
# znak * odpowiada cyfrze 2

wszystkie_dziesietne = []
with open("symbole.txt") as f:
    for line in f:
        line = line.strip()
        liczby = list(line)

        lista_trojkowa = []
        for liczba in liczby:
            if liczba == "o":
                lista_trojkowa.append(0)
            elif liczba == "+":
                lista_trojkowa.append(1)
            elif liczba == "*":
                lista_trojkowa.append(2)
        liczba_trojkowa = "".join(map(str, lista_trojkowa))

        liczba_dziesietna = int(liczba_trojkowa, 3)
        wszystkie_dziesietne.append(liczba_dziesietna)

suma_wszystkich = sum(wszystkie_dziesietne)
print(suma_wszystkich)

suma_trojkowa = na_trojkowy(suma_wszystkich)
suma_trojkowa = list(suma_trojkowa)

suma_zapis_trojkowy = []
for cyfra in suma_trojkowa:
    if cyfra == "0":
        suma_zapis_trojkowy.append("o")
    elif cyfra == "1":
        suma_zapis_trojkowy.append("+")
    elif cyfra == "2":
        suma_zapis_trojkowy.append("*")

wynik_symbole = "".join(map(str, suma_zapis_trojkowy))
print(wynik_symbole)
