with open("liczby.txt") as f:
    pierwsza_linia = list(map(int, f.readline().split()))
    druga_linia = list(map(int, f.readline().split()))

    wynik = 0
    for liczba_pierwsza in pierwsza_linia:
        for liczba in druga_linia:
            if liczba % liczba_pierwsza == 0:
                wynik += 1
                break

print(wynik)