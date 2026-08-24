with open("liczby.txt") as f:
    pierwsza_linia = list(map(int, f.readline().split()))
    druga_linia = list(map(int, f.readline().split()))

wynik = []

for liczba in druga_linia:
    temp = liczba

    dostepne = pierwsza_linia.copy()

    for pierwsza in dostepne:
        if temp % pierwsza == 0:
            temp //= pierwsza
            dostepne.remove(pierwsza)

    if temp == 1:
        wynik.append(liczba)

for i in wynik:
    print(i)