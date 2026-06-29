print("Zamiana z innego systemu liczbowego na dziesiętny:")
while True:
    liczba = (input("Podaj liczbę: "))
    podstawa = int(input("Podaj podstawę: "))
    wynik = int(liczba, podstawa)
    print(f"Wynik: {wynik}")