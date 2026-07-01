# znak o odpowiada cyfrze 0
# znak + odpowiada cyfrze 1
# znak * odpowiada cyfrze 2

wszystkie_liczby = []

with open("symbole.txt") as f:
    for line in f:
        line = line.strip()
        liczby = list(line)

        lista_trojkowa = []
        for liczba in liczby:
            if liczba == 'o':
                lista_trojkowa.append(0)
            elif liczba == '+':
                lista_trojkowa.append(1)
            elif liczba == '*':
                lista_trojkowa.append(2)

        liczba_trojkowa = "".join(map(str, lista_trojkowa))

        liczba = int(liczba_trojkowa, 3)
        wszystkie_liczby.append((liczba, line))

najwieksze = max(wszystkie_liczby)

print(najwieksze[0], najwieksze[1])


